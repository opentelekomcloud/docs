# OSE::RDS::Instance<a name="EN-US_TOPIC_0103361350"></a>

A resource for creating a relational database \(Relational Database Service\) instances.

A relational database service is a reliable, scalable, and easy-to-manage web service in the cloud.

## Required Properties<a name="section16891734131619"></a>

<a name="table243618914173"></a>
<table><thead align="left"><tr id="row1043718941715"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p643749201717"><a name="p643749201717"></a><a name="p643749201717"></a><strong id="b665219334321"><a name="b665219334321"></a><a name="b665219334321"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p164371961711"><a name="p164371961711"></a><a name="p164371961711"></a><strong id="b466693312322"><a name="b466693312322"></a><a name="b466693312322"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row24371992175"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p993635321714"><a name="p993635321714"></a><a name="p993635321714"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p493635371719"><a name="p493635371719"></a><a name="p493635371719"></a>Instance name</p>
<p id="p179361453151720"><a name="p179361453151720"></a><a name="p179361453151720"></a>String value expected.</p>
<p id="p2093615534179"><a name="p2093615534179"></a><a name="p2093615534179"></a>Updates cause replacement.</p>
<p id="p5936185371714"><a name="p5936185371714"></a><a name="p5936185371714"></a>The instance name of the same type instances under the same tenant must be unique.</p>
<p id="p493618534179"><a name="p493618534179"></a><a name="p493618534179"></a>Value range: The value is a string of 4 to 64 characters, case insensitive, which must start with a letter. An instance name can contain letters, digits, hyphens (-), or underscores (_). Other special characters cannot be included.</p>
</td>
</tr>
<tr id="row6437193177"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p3936953181719"><a name="p3936953181719"></a><a name="p3936953181719"></a>datastore_type</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p593695341712"><a name="p593695341712"></a><a name="p593695341712"></a>Database engine</p>
<p id="p6936753201710"><a name="p6936753201710"></a><a name="p6936753201710"></a>String value expected.</p>
<p id="p59364536173"><a name="p59364536173"></a><a name="p59364536173"></a>Updates cause replacement.</p>
<p id="p99364532170"><a name="p99364532170"></a><a name="p99364532170"></a>Allowed value: MySQL, PostgreSQL, or SQLServer</p>
</td>
</tr>
<tr id="row15437698176"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5936135313172"><a name="p5936135313172"></a><a name="p5936135313172"></a>datastore_version</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p169361553171715"><a name="p169361553171715"></a><a name="p169361553171715"></a>Instance version</p>
<p id="p49361953131716"><a name="p49361953131716"></a><a name="p49361953131716"></a>String value expected.</p>
<p id="p189361536176"><a name="p189361536176"></a><a name="p189361536176"></a>Updates cause replacement.</p>
<p id="p179361853181717"><a name="p179361853181717"></a><a name="p179361853181717"></a>Value range: The value contains a maximum of 64 characters and cannot be less than four characters.</p>
</td>
</tr>
<tr id="row12437159171710"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8936145301711"><a name="p8936145301711"></a><a name="p8936145301711"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p15936205361713"><a name="p15936205361713"></a><a name="p15936205361713"></a>Flavor ID</p>
<p id="p793616536178"><a name="p793616536178"></a><a name="p793616536178"></a>String value expected.</p>
<p id="p793645331712"><a name="p793645331712"></a><a name="p793645331712"></a>Can be updated without replacement.</p>
<p id="p293618532176"><a name="p293618532176"></a><a name="p293618532176"></a>Value range: The value cannot be empty. <span>The length of the character string is verified and the regular UUID regular check is performed.</span></p>
<div class="note" id="note196378151366"><a name="note196378151366"></a><a name="note196378151366"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p13815547133910"><a name="p13815547133910"></a><a name="p13815547133910"></a>For the value of this parameter, see <a href="how-to-obtain-the-flavor-value-of-resource-ose-rds-instance.md">How to Obtain the flavor Value of Resource OSE::RDS::Instance?</a>.</p>
</div></div>
</td>
</tr>
<tr id="row343879131712"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p184381912179"><a name="p184381912179"></a><a name="p184381912179"></a>volume</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1755754613219"><a name="p1755754613219"></a><a name="p1755754613219"></a>Disk information</p>
<p id="p1055713462217"><a name="p1055713462217"></a><a name="p1055713462217"></a>Map value expected.</p>
<p id="p355714461218"><a name="p355714461218"></a><a name="p355714461218"></a>Map properties:</p>
<a name="ul1137095452115"></a><a name="ul1137095452115"></a><ul id="ul1137095452115"><li>type<p id="p11115181532211"><a name="p11115181532211"></a><a name="p11115181532211"></a>Disk type</p>
<p id="p380091782219"><a name="p380091782219"></a><a name="p380091782219"></a>String value expected.</p>
<p id="p785672222215"><a name="p785672222215"></a><a name="p785672222215"></a>Updates cause replacement.</p>
<p id="p468515283224"><a name="p468515283224"></a><a name="p468515283224"></a>Allowed value: Common (SATA) and ULTRAHIGH (SSD), which are case sensitive.</p>
</li><li>size<p id="p336116315231"><a name="p336116315231"></a><a name="p336116315231"></a>Disk size</p>
<p id="p68757419234"><a name="p68757419234"></a><a name="p68757419234"></a>Integer value expected.</p>
<p id="p1686369172316"><a name="p1686369172316"></a><a name="p1686369172316"></a>Unit: GB</p>
<p id="p47578181232"><a name="p47578181232"></a><a name="p47578181232"></a>Can be updated without replacement.</p>
<p id="p6728192472313"><a name="p6728192472313"></a><a name="p6728192472313"></a>Value range: The value ranges from 100 to 2000 and must be an integer multiple of 10.</p>
</li></ul>
</td>
</tr>
<tr id="row443817971716"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p14810651112320"><a name="p14810651112320"></a><a name="p14810651112320"></a>region</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p168101051132320"><a name="p168101051132320"></a><a name="p168101051132320"></a>Region ID</p>
<p id="p1281075112312"><a name="p1281075112312"></a><a name="p1281075112312"></a>String value expected.</p>
<p id="p17810165142312"><a name="p17810165142312"></a><a name="p17810165142312"></a>Updates cause replacement.</p>
<p id="p16810155122316"><a name="p16810155122316"></a><a name="p16810155122316"></a>Value range: The value cannot be empty.</p>
</td>
</tr>
<tr id="row943814914171"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p2081055132310"><a name="p2081055132310"></a><a name="p2081055132310"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1081085116230"><a name="p1081085116230"></a><a name="p1081085116230"></a>ID of an available zone</p>
<p id="p281013511235"><a name="p281013511235"></a><a name="p281013511235"></a>String value expected.</p>
<p id="p128101451152320"><a name="p128101451152320"></a><a name="p128101451152320"></a>Updates cause replacement.</p>
<p id="p15810115112312"><a name="p15810115112312"></a><a name="p15810115112312"></a>Value range: The value cannot be empty.</p>
</td>
</tr>
<tr id="row11438109161719"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p943889161713"><a name="p943889161713"></a><a name="p943889161713"></a>nics</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1357314131246"><a name="p1357314131246"></a><a name="p1357314131246"></a>Subnet information</p>
<p id="p7573171313243"><a name="p7573171313243"></a><a name="p7573171313243"></a>Map value expected.</p>
<p id="p057321316245"><a name="p057321316245"></a><a name="p057321316245"></a>Map properties:</p>
<a name="ul189297204242"></a><a name="ul189297204242"></a><ul id="ul189297204242"><li>subnet<p id="p101131628162420"><a name="p101131628162420"></a><a name="p101131628162420"></a>Subnet ID</p>
<p id="p342972962415"><a name="p342972962415"></a><a name="p342972962415"></a>String value expected.</p>
<p id="p1774083417241"><a name="p1774083417241"></a><a name="p1774083417241"></a>Updates cause replacement.</p>
<p id="p166471540192420"><a name="p166471540192420"></a><a name="p166471540192420"></a>Value range: <span>The value cannot be empty. The length of the character string must be verified through the regular UUID check.</span></p>
</li></ul>
</td>
</tr>
<tr id="row1443817991712"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1248211352512"><a name="p1248211352512"></a><a name="p1248211352512"></a>vpc</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p144821735258"><a name="p144821735258"></a><a name="p144821735258"></a>ID of a VPC</p>
<p id="p1848253132512"><a name="p1848253132512"></a><a name="p1848253132512"></a>String value expected.</p>
<p id="p24821334250"><a name="p24821334250"></a><a name="p24821334250"></a>Updates cause replacement.</p>
<p id="p1048253132510"><a name="p1048253132510"></a><a name="p1048253132510"></a>Value range: The value cannot be empty. The length of the character string must be verified through the regular UUID check.</p>
</td>
</tr>
<tr id="row14382941715"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1543172014251"><a name="p1543172014251"></a><a name="p1543172014251"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p11431132011252"><a name="p11431132011252"></a><a name="p11431132011252"></a>Security group to which an instance belongs</p>
<p id="p74311020182511"><a name="p74311020182511"></a><a name="p74311020182511"></a>String value expected.</p>
<p id="p1143110204254"><a name="p1143110204254"></a><a name="p1143110204254"></a>Updates cause replacement.</p>
<p id="p1143112018257"><a name="p1143112018257"></a><a name="p1143112018257"></a>Value range: The value cannot be empty. The length of the character string must be verified through the regular UUID check.</p>
</td>
</tr>
<tr id="row194381496171"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p463294062511"><a name="p463294062511"></a><a name="p463294062511"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p763214052512"><a name="p763214052512"></a><a name="p763214052512"></a>Password of the database <strong id="b1585425535916"><a name="b1585425535916"></a><a name="b1585425535916"></a>root</strong> user</p>
<p id="p463211400253"><a name="p463211400253"></a><a name="p463211400253"></a>String value expected.</p>
<p id="p96321140192516"><a name="p96321140192516"></a><a name="p96321140192516"></a>Updates cause replacement.</p>
<p id="p14632840102515"><a name="p14632840102515"></a><a name="p14632840102515"></a>Value range: The value is a string of 8 to32 characters consisting of uppercase letters, lowercase letters, digits, and special characters ~!@#%^*-_=+?. The password must contain uppercase letters, lowercase letters, digits, and at least one special character.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section232328112614"></a>

<a name="table11575444102610"></a>
<table><thead align="left"><tr id="row18577174482615"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p148781554122620"><a name="p148781554122620"></a><a name="p148781554122620"></a><strong id="b2293104183217"><a name="b2293104183217"></a><a name="b2293104183217"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p1487825413260"><a name="p1487825413260"></a><a name="p1487825413260"></a><strong id="b1295941163214"><a name="b1295941163214"></a><a name="b1295941163214"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row357744422619"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1516317125275"><a name="p1516317125275"></a><a name="p1516317125275"></a>db_port</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p13163812112718"><a name="p13163812112718"></a><a name="p13163812112718"></a>Port number of the database</p>
<p id="p0163201232720"><a name="p0163201232720"></a><a name="p0163201232720"></a>Integer value expected.</p>
<p id="p416331212274"><a name="p416331212274"></a><a name="p416331212274"></a>The default value is <strong id="b118681511913"><a name="b118681511913"></a><a name="b118681511913"></a>8036</strong>.</p>
<p id="p216311242713"><a name="p216311242713"></a><a name="p216311242713"></a>Cannot be updated.</p>
</td>
</tr>
<tr id="row1057714445264"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p157794412267"><a name="p157794412267"></a><a name="p157794412267"></a>backup_strategy</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p4256230112715"><a name="p4256230112715"></a><a name="p4256230112715"></a>Advanced backup policy</p>
<p id="p15256123020278"><a name="p15256123020278"></a><a name="p15256123020278"></a>Map value expected.</p>
<p id="p1725663042717"><a name="p1725663042717"></a><a name="p1725663042717"></a>Map properties:</p>
<a name="ul976693722719"></a><a name="ul976693722719"></a><ul id="ul976693722719"><li>start_time<p id="p3835114472711"><a name="p3835114472711"></a><a name="p3835114472711"></a>Start time: Automatic backup will be triggered within one hour of the start time.</p>
<p id="p148352044162715"><a name="p148352044162715"></a><a name="p148352044162715"></a>String value expected.</p>
<p id="p128355445272"><a name="p128355445272"></a><a name="p128355445272"></a>Updates cause replacement.</p>
<p id="p2083520445277"><a name="p2083520445277"></a><a name="p2083520445277"></a>Value range: The value cannot be empty. The value must be in hh:mm:ss format and valid. The current time is the UTC time.</p>
</li><li>days<p id="p02281050133714"><a name="p02281050133714"></a><a name="p02281050133714"></a>The number of days for which backup files can be saved.</p>
<p id="p3138154103713"><a name="p3138154103713"></a><a name="p3138154103713"></a>Integer value expected.</p>
<p id="p144411133813"><a name="p144411133813"></a><a name="p144411133813"></a>Updates cause replacement.</p>
<p id="p119900673815"><a name="p119900673815"></a><a name="p119900673815"></a>Value range: 0 to 35. When this parameter is set to the default value or <strong id="b103887391032"><a name="b103887391032"></a><a name="b103887391032"></a>0</strong>, the automatic backup policy is not configured.</p>
</li></ul>
</td>
</tr>
<tr id="row1157716442264"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1357734414261"><a name="p1357734414261"></a><a name="p1357734414261"></a>ha</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p88641212124019"><a name="p88641212124019"></a><a name="p88641212124019"></a>HA configuration parameter, which is used for creating an HA instance.</p>
<p id="p7864161217402"><a name="p7864161217402"></a><a name="p7864161217402"></a>Map value expected.</p>
<p id="p138641912194015"><a name="p138641912194015"></a><a name="p138641912194015"></a>Map properties:</p>
<a name="ul1811324104013"></a><a name="ul1811324104013"></a><ul id="ul1811324104013"><li>enable<p id="p1044994111404"><a name="p1044994111404"></a><a name="p1044994111404"></a>HA configuration parameters</p>
<p id="p14491641194010"><a name="p14491641194010"></a><a name="p14491641194010"></a>Boolean value expected.</p>
<p id="p13449174111403"><a name="p13449174111403"></a><a name="p13449174111403"></a>Updates cause replacement.</p>
</li><li>replication_mode<p id="p994375244016"><a name="p994375244016"></a><a name="p994375244016"></a>Synchronization parameter of the standby node</p>
<p id="p129431652174010"><a name="p129431652174010"></a><a name="p129431652174010"></a>String value expected.</p>
<p id="p3943252184012"><a name="p3943252184012"></a><a name="p3943252184012"></a>Updates cause replacement.</p>
<div class="p" id="p1094314527403"><a name="p1094314527403"></a><a name="p1094314527403"></a>Value range: The value cannot be empty.<a name="ul1512741794117"></a><a name="ul1512741794117"></a><ul id="ul1512741794117"><li>MySQL : The value can be <strong id="b4939059052"><a name="b4939059052"></a><a name="b4939059052"></a>async </strong>or <strong id="b59392059959"><a name="b59392059959"></a><a name="b59392059959"></a>semisync</strong>.</li><li>PostgreSQL: The value can be<strong id="b695112714613"><a name="b695112714613"></a><a name="b695112714613"></a> async</strong> or <strong id="b19951073615"><a name="b19951073615"></a><a name="b19951073615"></a>sync</strong>.</li></ul>
</div>
</li></ul>
<div class="notice" id="note1781755104111"><a name="note1781755104111"></a><a name="note1781755104111"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1878185517415"><a name="p1878185517415"></a><a name="p1878185517415"></a>Microsoft SQL Server does not support the creation of HA instances. Therefore, this parameter is not involved.</p>
</div></div>
</td>
</tr>
<tr id="row19577144482610"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p18425628154213"><a name="p18425628154213"></a><a name="p18425628154213"></a>replica_of</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p154258289424"><a name="p154258289424"></a><a name="p154258289424"></a>Read-only copy configuration parameter (mandatory when a read-only copy is created).</p>
<p id="p10425828124218"><a name="p10425828124218"></a><a name="p10425828124218"></a>String value expected.</p>
<p id="p24251281421"><a name="p24251281421"></a><a name="p24251281421"></a>Cannot be updated.</p>
<p id="p124259281429"><a name="p124259281429"></a><a name="p124259281429"></a>Value range: instance ID of the primary instance</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section11761344144216"></a>

<a name="table31178318438"></a>
<table><thead align="left"><tr id="row211714311434"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="p1911711319438"><a name="p1911711319438"></a><a name="p1911711319438"></a><strong id="b248818463327"><a name="b248818463327"></a><a name="b248818463327"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="p4117103184315"><a name="p4117103184315"></a><a name="p4117103184315"></a><strong id="b2048974673213"><a name="b2048974673213"></a><a name="b2048974673213"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row171171539437"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p451785515434"><a name="p451785515434"></a><a name="p451785515434"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p8517955114310"><a name="p8517955114310"></a><a name="p8517955114310"></a>Database instance name</p>
</td>
</tr>
<tr id="row11117103194318"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p7519165544319"><a name="p7519165544319"></a><a name="p7519165544319"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p15519125564311"><a name="p15519125564311"></a><a name="p15519125564311"></a>Specification information</p>
</td>
</tr>
<tr id="row1117331439"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p12519205574318"><a name="p12519205574318"></a><a name="p12519205574318"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p951919550431"><a name="p951919550431"></a><a name="p951919550431"></a>Connection address of an instance. The value exists only after an ECS is created successfully. In other cases, the value is an empty string.</p>
</td>
</tr>
<tr id="row61171632439"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p175191755194320"><a name="p175191755194320"></a><a name="p175191755194320"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p851925518435"><a name="p851925518435"></a><a name="p851925518435"></a>Instance type. The value can be <strong id="b13106161618712"><a name="b13106161618712"></a><a name="b13106161618712"></a>master</strong>,<strong id="b191066160713"><a name="b191066160713"></a><a name="b191066160713"></a> slave</strong>, or <strong id="b171069161679"><a name="b171069161679"></a><a name="b171069161679"></a>readreplica</strong>.</p>
</td>
</tr>
<tr id="row1011814312439"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p851914550433"><a name="p851914550433"></a><a name="p851914550433"></a>backupStrategy</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p2519155594311"><a name="p2519155594311"></a><a name="p2519155594311"></a>Advanced backup policy</p>
</td>
</tr>
<tr id="row211819311437"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p5519955164315"><a name="p5519955164315"></a><a name="p5519955164315"></a>slaveId</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p1451955512439"><a name="p1451955512439"></a><a name="p1451955512439"></a>ID of the secondary instance.</p>
</td>
</tr>
<tr id="row131189317436"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p75191455124318"><a name="p75191455124318"></a><a name="p75191455124318"></a>ha</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p85191355134315"><a name="p85191355134315"></a><a name="p85191355134315"></a>HA information. This parameter is returned when the HA instance is obtained.</p>
</td>
</tr>
<tr id="row20118238438"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="p252095544312"><a name="p252095544312"></a><a name="p252095544312"></a>replicaOf</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="p115201055204318"><a name="p115201055204318"></a><a name="p115201055204318"></a>This parameter is returned only when a read-only copy is obtained.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section195131339447"></a>

```
heat_template_version: 2014-10-16
...
resources:
  the_resource:
    type: OSE::RDS::Instance
    properties:
      name: String
      region: String
      availability_zone: String
      nics:
        subnet: String
      volume:
        type: String
        size: Number
      security_group: String
      vpc: String
      datastore_type: String
      datastore_version: String
      flavor: String
      password: String
```

