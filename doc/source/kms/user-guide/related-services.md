# Related Services<a name="kms_01_0016"></a>

## OBS<a name="section51930849101821"></a>

KMS provides central management and control capabilities of CMKs for Object Storage Service \(OBS\). It is used for server-side encryption with KMS-managed keys \(SSE-KMS\) function of OBS.

## EVS<a name="section5520572894054"></a>

KMS provides central management and control capabilities of CMKs for Elastic Volume Service \(EVS\). It is applied to the encryption function of EVS.

## IMS<a name="section25980404183412"></a>

KMS provides central management and control capabilities of CMKs for Image Management Service \(IMS\). It is applied to the private image encryption function of IMS.

## SFS<a name="section4141511085"></a>

KMS provides central management and control capabilities of CMKs for Scalable File Service \(SFS\). It is applied to the file system encryption function of SFS.

## RDS<a name="section8605249175317"></a>

KMS provides central management and control capabilities of CMKs for Relational Database Service \(RDS\). It is applied to the disk encryption of database instances in RDS.

## CTS<a name="section2258398103347"></a>

Cloud Trace Service \(CTS\) provides you with a history of KMS operations. After enabling the CTS service, you can view all generated traces to review and audit performed KMS operations. For details, see the  _Cloud Trace Service User Guide_.

**Table  1**  KMS operations supported by CTS

<a name="table52008441163754"></a>
<table><thead align="left"><tr id="row35586605163754"><th class="cellrowborder" valign="top" width="35.55%" id="mcps1.2.4.1.1"><p id="p63942737163754"><a name="p63942737163754"></a><a name="p63942737163754"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.2"><p id="p16413837105650"><a name="p16413837105650"></a><a name="p16413837105650"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.28%" id="mcps1.2.4.1.3"><p id="p31883243184927"><a name="p31883243184927"></a><a name="p31883243184927"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row23849839163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p52788769163754"><a name="p52788769163754"></a><a name="p52788769163754"></a>Creating a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p48568046105650"><a name="p48568046105650"></a><a name="p48568046105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p61263700163754"><a name="p61263700163754"></a><a name="p61263700163754"></a>createKey</p>
</td>
</tr>
<tr id="row14502393163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p33843219163754"><a name="p33843219163754"></a><a name="p33843219163754"></a>Creating a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p39734583105650"><a name="p39734583105650"></a><a name="p39734583105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p29275668163754"><a name="p29275668163754"></a><a name="p29275668163754"></a>createDataKey</p>
</td>
</tr>
<tr id="row62154424163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p1343620163754"><a name="p1343620163754"></a><a name="p1343620163754"></a>Creating a plaintext-free DEK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p42590852105650"><a name="p42590852105650"></a><a name="p42590852105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p16494320163754"><a name="p16494320163754"></a><a name="p16494320163754"></a>createDataKeyWithoutPlaintext</p>
</td>
</tr>
<tr id="row14231157163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p11873035163754"><a name="p11873035163754"></a><a name="p11873035163754"></a>Enabling a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p44436112105650"><a name="p44436112105650"></a><a name="p44436112105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p41132017163754"><a name="p41132017163754"></a><a name="p41132017163754"></a>enableKey</p>
</td>
</tr>
<tr id="row34643839163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p54687563163754"><a name="p54687563163754"></a><a name="p54687563163754"></a>Disabling a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p47453406105650"><a name="p47453406105650"></a><a name="p47453406105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p41892520163754"><a name="p41892520163754"></a><a name="p41892520163754"></a>disableKey</p>
</td>
</tr>
<tr id="row41488368163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p5114667163754"><a name="p5114667163754"></a><a name="p5114667163754"></a>Encrypting a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p32468345105650"><a name="p32468345105650"></a><a name="p32468345105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p33768047163754"><a name="p33768047163754"></a><a name="p33768047163754"></a>encryptDataKey</p>
</td>
</tr>
<tr id="row35476970163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p55062302163754"><a name="p55062302163754"></a><a name="p55062302163754"></a>Decrypting a DEK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p47103925105650"><a name="p47103925105650"></a><a name="p47103925105650"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p14668965163754"><a name="p14668965163754"></a><a name="p14668965163754"></a>decryptDataKey</p>
</td>
</tr>
<tr id="row64911828163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p23366748163754"><a name="p23366748163754"></a><a name="p23366748163754"></a>Scheduling the deletion of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p27342688105640"><a name="p27342688105640"></a><a name="p27342688105640"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p22561525163754"><a name="p22561525163754"></a><a name="p22561525163754"></a>scheduleKeyDeletion</p>
</td>
</tr>
<tr id="row1727137163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p5680422163754"><a name="p5680422163754"></a><a name="p5680422163754"></a>Canceling the scheduled deletion of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p165290105640"><a name="p165290105640"></a><a name="p165290105640"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p51285903163754"><a name="p51285903163754"></a><a name="p51285903163754"></a>cancelKeyDeletion</p>
</td>
</tr>
<tr id="row58919945163754"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p7786245163754"><a name="p7786245163754"></a><a name="p7786245163754"></a>Generating random numbers</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p13388557105640"><a name="p13388557105640"></a><a name="p13388557105640"></a>rng</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p64625516163754"><a name="p64625516163754"></a><a name="p64625516163754"></a>genRandom</p>
</td>
</tr>
<tr id="row45895703173414"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p26564439173414"><a name="p26564439173414"></a><a name="p26564439173414"></a>Changing the alias of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p4235960173414"><a name="p4235960173414"></a><a name="p4235960173414"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p7568481173414"><a name="p7568481173414"></a><a name="p7568481173414"></a>updateKeyAlias</p>
</td>
</tr>
<tr id="row25019558173421"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p31313880173420"><a name="p31313880173420"></a><a name="p31313880173420"></a>Changing the description of a CMK</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p53396313173420"><a name="p53396313173420"></a><a name="p53396313173420"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p30134091173420"><a name="p30134091173420"></a><a name="p30134091173420"></a>updateKeyDescription</p>
</td>
</tr>
<tr id="row15292987154533"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p30772396154533"><a name="p30772396154533"></a><a name="p30772396154533"></a>Prompting risks about CMK deletion</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p9536142154533"><a name="p9536142154533"></a><a name="p9536142154533"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p34230024154533"><a name="p34230024154533"></a><a name="p34230024154533"></a>deleteKeyRiskTips</p>
</td>
</tr>
<tr id="row118674191468"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p4502456111613"><a name="p4502456111613"></a><a name="p4502456111613"></a>Importing key material</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p29154680111613"><a name="p29154680111613"></a><a name="p29154680111613"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p12718897111613"><a name="p12718897111613"></a><a name="p12718897111613"></a>importKeyMaterial</p>
</td>
</tr>
<tr id="row1972712529519"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p3071733111180"><a name="p3071733111180"></a><a name="p3071733111180"></a>Deleting key material</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p507586811180"><a name="p507586811180"></a><a name="p507586811180"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p849216211180"><a name="p849216211180"></a><a name="p849216211180"></a>deleteImportedKeyMaterial</p>
</td>
</tr>
<tr id="row62552846173423"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p30466396173422"><a name="p30466396173422"></a><a name="p30466396173422"></a>Creating a grant</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p51858981173422"><a name="p51858981173422"></a><a name="p51858981173422"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p39827894173422"><a name="p39827894173422"></a><a name="p39827894173422"></a>createGrant</p>
</td>
</tr>
<tr id="row22116876173428"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p15830208173427"><a name="p15830208173427"></a><a name="p15830208173427"></a>Retiring a grant</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p7178472173427"><a name="p7178472173427"></a><a name="p7178472173427"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p44585373173427"><a name="p44585373173427"></a><a name="p44585373173427"></a>retireGrant</p>
</td>
</tr>
<tr id="row16246148173430"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p38348503173429"><a name="p38348503173429"></a><a name="p38348503173429"></a>Revoking a grant</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p19221025173429"><a name="p19221025173429"></a><a name="p19221025173429"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p13399212173429"><a name="p13399212173429"></a><a name="p13399212173429"></a>revokeGrant</p>
</td>
</tr>
<tr id="row1690719182415"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p189051932418"><a name="p189051932418"></a><a name="p189051932418"></a>Adding a tag</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p3268133112514"><a name="p3268133112514"></a><a name="p3268133112514"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p16913194242"><a name="p16913194242"></a><a name="p16913194242"></a>createKeyTag</p>
</td>
</tr>
<tr id="row1022082312241"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p19220182372414"><a name="p19220182372414"></a><a name="p19220182372414"></a>Deleting a tag</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p627113331253"><a name="p627113331253"></a><a name="p627113331253"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p1522092372414"><a name="p1522092372414"></a><a name="p1522092372414"></a>deleteKeyTag</p>
</td>
</tr>
<tr id="row375102702412"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p1375227132412"><a name="p1375227132412"></a><a name="p1375227132412"></a>Adding or deleting tags in batches</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p1327112339254"><a name="p1327112339254"></a><a name="p1327112339254"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p2751627132417"><a name="p2751627132417"></a><a name="p2751627132417"></a>batchCreateKeyTags</p>
</td>
</tr>
<tr id="row095291992514"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p16952101916250"><a name="p16952101916250"></a><a name="p16952101916250"></a>Batch deleting tags</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p13273153319251"><a name="p13273153319251"></a><a name="p13273153319251"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p1395291922519"><a name="p1395291922519"></a><a name="p1395291922519"></a>batchDeleteKeyTags</p>
</td>
</tr>
<tr id="row28107416617"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p118111941561"><a name="p118111941561"></a><a name="p118111941561"></a>Enabling key rotation</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p1781164115614"><a name="p1781164115614"></a><a name="p1781164115614"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p1681115411767"><a name="p1681115411767"></a><a name="p1681115411767"></a>enableKeyRotation</p>
</td>
</tr>
<tr id="row157001347869"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p87003476619"><a name="p87003476619"></a><a name="p87003476619"></a>Modifying the rotation interval</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p1870015476615"><a name="p1870015476615"></a><a name="p1870015476615"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p470017476615"><a name="p470017476615"></a><a name="p470017476615"></a>updateKeyRotationInterval</p>
</td>
</tr>
<tr id="row1755115451764"><td class="cellrowborder" valign="top" width="35.55%" headers="mcps1.2.4.1.1 "><p id="p95511245663"><a name="p95511245663"></a><a name="p95511245663"></a>Disabling key rotation</p>
</td>
<td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p55518451965"><a name="p55518451965"></a><a name="p55518451965"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="41.28%" headers="mcps1.2.4.1.3 "><p id="p2551184516619"><a name="p2551184516619"></a><a name="p2551184516619"></a>disableKeyRotation</p>
</td>
</tr>
</tbody>
</table>

## IAM<a name="section4573770192847"></a>

Identity and Access Management \(IAM\) provides the permission management function for KMS. Only users who have KMS Administrator permissions can use KMS. To apply for KMS Administrator permissions, contact a user with Security Administrator permissions. For details, see the  _Identity and Access Management User Guide_.

