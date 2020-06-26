# SDRS Basic Concepts<a name="sdrs_pro_0013"></a>

**Table  1**  SDRS basic concepts

<a name="table192300118464"></a>
<table><thead align="left"><tr id="row182331513461"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.3.1.1"><p id="p202337174613"><a name="p202337174613"></a><a name="p202337174613"></a>Concept</p>
</th>
<th class="cellrowborder" valign="top" width="87%" id="mcps1.2.3.1.2"><p id="p18233141104610"><a name="p18233141104610"></a><a name="p18233141104610"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row182331216462"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p523319115463"><a name="p523319115463"></a><a name="p523319115463"></a>Production site</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p8233215465"><a name="p8233215465"></a><a name="p8233215465"></a>A production site is the data center that independently carries services in normal cases. For SDRS, it is the AZ where your <span id="text164511550123112"><a name="text164511550123112"></a><a name="text164511550123112"></a>server</span><span id="text1240115317318"><a name="text1240115317318"></a><a name="text1240115317318"></a></span>s locate. This parameter is specified when you create a protection group.</p>
</td>
</tr>
<tr id="row4233141144613"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p32338110461"><a name="p32338110461"></a><a name="p32338110461"></a>DR site</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p1683143644912"><a name="p1683143644912"></a><a name="p1683143644912"></a>A DR site is the data center that does not carry services when the production site works properly. It is used to back up data in real time. When the production site fails (planned or unexpected), the DR site can take over the services after a failover. It can reside in the same city as the service management center or in another city.</p>
<p id="p1856723454410"><a name="p1856723454410"></a><a name="p1856723454410"></a>In this version, the production and DR sites must be in different AZs in the same region.</p>
</td>
</tr>
<tr id="row21724564311"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p111804534315"><a name="p111804534315"></a><a name="p111804534315"></a>Protection group</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p12201619124211"><a name="p12201619124211"></a><a name="p12201619124211"></a>Used to manage a group of <span id="text519764262812"><a name="text519764262812"></a><a name="text519764262812"></a>server</span><span id="text119814217284"><a name="text119814217284"></a><a name="text119814217284"></a></span>s to be replicated. One protection group is for <span id="text17623147122813"><a name="text17623147122813"></a><a name="text17623147122813"></a>server</span><span id="text2062314718288"><a name="text2062314718288"></a><a name="text2062314718288"></a></span>s in one VPC. If you have multiple VPCs, you need to create multiple protection groups.</p>
</td>
</tr>
<tr id="row175573810431"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p167551438164310"><a name="p167551438164310"></a><a name="p167551438164310"></a>Protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p6632154244215"><a name="p6632154244215"></a><a name="p6632154244215"></a>Indicates a <span id="text0418195212284"><a name="text0418195212284"></a><a name="text0418195212284"></a>server</span><span id="text124191252192811"><a name="text124191252192811"></a><a name="text124191252192811"></a></span> and its replication <span id="text6786152983817"><a name="text6786152983817"></a><a name="text6786152983817"></a>server</span><span id="text147871229133811"><a name="text147871229133811"></a><a name="text147871229133811"></a></span>. A protected instance belongs to one protection group. Therefore, the production site and DR site of the protected instance are the same as those of the protected instance's protection group.</p>
</td>
</tr>
<tr id="row595293294311"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1195423244314"><a name="p1195423244314"></a><a name="p1195423244314"></a>Replication pair</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p83991449114215"><a name="p83991449114215"></a><a name="p83991449114215"></a>Indicates a disk and its replication disk. A replication pair belongs to one protection group and can be attached to a protected instance in this protection group.</p>
</td>
</tr>
<tr id="row223320174618"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p2233714468"><a name="p2233714468"></a><a name="p2233714468"></a>Planned failover</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p723319116466"><a name="p723319116466"></a><a name="p723319116466"></a>You can temporarily stop <span id="text140192710395"><a name="text140192710395"></a><a name="text140192710395"></a>server</span><span id="text194042703911"><a name="text194042703911"></a><a name="text194042703911"></a></span>s at the production site and then perform a planned failover to fail over services from the production site to the DR site. After the planned failover, data synchronization continues, but the DR direction is changed (from the DR site to the production site). Servers and disks at the DR site are ready to start.</p>
</td>
</tr>
<tr id="row1546215109452"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p846313103456"><a name="p846313103456"></a><a name="p846313103456"></a>Failover</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p1246361024510"><a name="p1246361024510"></a><a name="p1246361024510"></a>The system forcibly stops the servers and disks at the production site and sets the servers and disks at the DR site to ready-to-start state. This action affects all the protected instances in the protection group. After the failover, you need to start the <span id="text14460124812414"><a name="text14460124812414"></a><a name="text14460124812414"></a>server</span><span id="text046113484418"><a name="text046113484418"></a><a name="text046113484418"></a></span>s at the DR site. The protection group status changes to <strong id="b212843216498"><a name="b212843216498"></a><a name="b212843216498"></a>Failover complete</strong>, and data synchronization of the protection group stops. You need to enable protection again to restore data synchronization.</p>
</td>
</tr>
<tr id="row5525142456"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1952181410458"><a name="p1952181410458"></a><a name="p1952181410458"></a>Enabling protection</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p1055610204616"><a name="p1055610204616"></a><a name="p1055610204616"></a>This operation can be performed after a protection group is created or data synchronization stops. Once the protection is enabled, the data synchronization starts, and the synchronization progress is displayed on the web page. This operation affects all protected instances and replication pairs in the protection group.</p>
<p id="p8924135210271"><a name="p8924135210271"></a><a name="p8924135210271"></a>When you click <strong id="b20234735140549"><a name="b20234735140549"></a><a name="b20234735140549"></a>Enable Protection</strong>, the status of the protection group changes to <strong id="b987555510526"><a name="b987555510526"></a><a name="b987555510526"></a>Synchronizing</strong>, and <strong id="b1283060450635"><a name="b1283060450635"></a><a name="b1283060450635"></a>Disable Protection</strong> is not available.</p>
</td>
</tr>
<tr id="row1322414102710"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1422161492715"><a name="p1422161492715"></a><a name="p1422161492715"></a>Enabling protection again</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p1544717334274"><a name="p1544717334274"></a><a name="p1544717334274"></a>This operation can be performed after a failover. Once the protection is enabled again, the data synchronization starts, and the synchronization progress is displayed on the web page. This operation affects all protected instances and replication pairs in the protection group.</p>
<p id="p18210610132814"><a name="p18210610132814"></a><a name="p18210610132814"></a>When you click <strong id="b8423527060354"><a name="b8423527060354"></a><a name="b8423527060354"></a>Reprotect</strong> after a failover, the status of the protection group changes to <strong id="b1931120253541"><a name="b1931120253541"></a><a name="b1931120253541"></a>Re-protecting</strong>, and <strong id="b8423527060519"><a name="b8423527060519"></a><a name="b8423527060519"></a>Disable Protection</strong> becomes unavailable.</p>
</td>
</tr>
<tr id="row118261636123013"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p182663611304"><a name="p182663611304"></a><a name="p182663611304"></a>Disabling protection</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p1986383612458"><a name="p1986383612458"></a><a name="p1986383612458"></a>Can be performed after the data synchronization is complete. Once the protection is disabled, the data synchronization stops, and the protection status of the protection group changes to <strong id="b1390754024719"><a name="b1390754024719"></a><a name="b1390754024719"></a>Available</strong>.</p>
</td>
</tr>
<tr id="row2048791794512"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1548712173455"><a name="p1548712173455"></a><a name="p1548712173455"></a>Attaching a replication pair to a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p204871517144517"><a name="p204871517144517"></a><a name="p204871517144517"></a>Indicates to attach the two disks in a replication pair to the two <span id="text1310111217423"><a name="text1310111217423"></a><a name="text1310111217423"></a>server</span><span id="text1510111217421"><a name="text1510111217421"></a><a name="text1510111217421"></a></span>s in a protected instance.</p>
</td>
</tr>
<tr id="row1516919346466"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p31692342467"><a name="p31692342467"></a><a name="p31692342467"></a>Detaching a replication pair from a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p6169734104610"><a name="p6169734104610"></a><a name="p6169734104610"></a>Indicates to detach the two disks in a replication pair from the two <span id="text9335181794220"><a name="text9335181794220"></a><a name="text9335181794220"></a>server</span><span id="text5336161713426"><a name="text5336161713426"></a><a name="text5336161713426"></a></span>s in a protected instance.</p>
</td>
</tr>
<tr id="row1190919560"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1693912410611"><a name="p1693912410611"></a><a name="p1693912410611"></a>DR direction</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p493904118611"><a name="p493904118611"></a><a name="p493904118611"></a>Indicates the data replication direction. The data replication is from the production site to the DR site when users create a protection group.</p>
<p id="p1657413919310"><a name="p1657413919310"></a><a name="p1657413919310"></a>After you perform a planned failover, services at the production site are failed over to the DR site, and services at the DR site are failed over to the production site.</p>
</td>
</tr>
<tr id="row1525310241663"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1939164117611"><a name="p1939164117611"></a><a name="p1939164117611"></a>Protection group status</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p583914331495"><a name="p583914331495"></a><a name="p583914331495"></a>Indicates the status of a protection group when users perform an operation on the protection group, such as creating or deleting a protection group, enabling or disabling protection, or performing a planned failover or failover.</p>
<p id="p109396410610"><a name="p109396410610"></a><a name="p109396410610"></a>For details, see the protection group status section in the Appendixes of <em id="i96473407189"><a name="i96473407189"></a><a name="i96473407189"></a>Storage Disaster Recovery Service API Reference</em>.</p>
</td>
</tr>
<tr id="row7392122814612"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p8939114115612"><a name="p8939114115612"></a><a name="p8939114115612"></a>Synchronization status</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p199391411964"><a name="p199391411964"></a><a name="p199391411964"></a>Indicates the status of the data replication between the production and DR sites.</p>
</td>
</tr>
<tr id="row122051338663"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p1793913411565"><a name="p1793913411565"></a><a name="p1793913411565"></a>VPC</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p093912414613"><a name="p093912414613"></a><a name="p093912414613"></a>Indicates the VPC of the protection group. A VPC facilitates internal network management and configuration, allowing secure and quick modifications to networks. The <span id="text4243540144212"><a name="text4243540144212"></a><a name="text4243540144212"></a>server</span><span id="text192431540194219"><a name="text192431540194219"></a><a name="text192431540194219"></a></span>s in the same VPC can communicate with each other, but those in different VPCs cannot communicate with each other by default.</p>
</td>
</tr>
<tr id="row134398123020"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p143430812303"><a name="p143430812303"></a><a name="p143430812303"></a>VBD</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p14343118103015"><a name="p14343118103015"></a><a name="p14343118103015"></a>Virtual Block Device (VBD) is the default type of disks. Disks of the VBD type support only simple Small Computer System Interface (SCSI) read and write commands. This disk type applies to enterprise office applications as well as development and testing scenarios.</p>
</td>
</tr>
<tr id="row143591252301"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p03591520308"><a name="p03591520308"></a><a name="p03591520308"></a>SCSI</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p335955173018"><a name="p335955173018"></a><a name="p335955173018"></a>SCSI is another disk type. Disks of this type support transparent SCSI command transmission to allow the server OS to directly access the underlying storage media. In addition to simple SCSI read and write commands, SCSI disks also support advanced SCSI commands, for example, persistent lock reservation command, suitable for using the lock mechanism to ensure data security for cluster applications.</p>
</td>
</tr>
<tr id="row1379211441277"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p37921544142710"><a name="p37921544142710"></a><a name="p37921544142710"></a>RPO</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p87922449274"><a name="p87922449274"></a><a name="p87922449274"></a>Indicates recovery point objective. It is a service switchover policy, minimizing data loss during DR switchover. The data recovery point is used as the objective to ensure that the data used for DR switchover is the latest backup data.</p>
</td>
</tr>
<tr id="row374524813271"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p12745134811272"><a name="p12745134811272"></a><a name="p12745134811272"></a>RTO</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p674516489275"><a name="p674516489275"></a><a name="p674516489275"></a>Indicates recovery time objective. It is the target time on the recovery of interrupted key businesses to an acceptable level. RTO is set to minimize an interruption's impacts on the services. For SDRS, recovery time objective (RTO) refers to the period from the time when users perform a planned failover or failover at the production site to the time when the <span id="text68390435434"><a name="text68390435434"></a><a name="text68390435434"></a>server</span><span id="text12840104374320"><a name="text12840104374320"></a><a name="text12840104374320"></a></span>s at the DR site start to run. This period does not include any time for DNS configuration, security group configuration, or customer script execution, and is within 30 minutes.</p>
</td>
</tr>
<tr id="row8161855103017"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.3.1.1 "><p id="p181611455123015"><a name="p181611455123015"></a><a name="p181611455123015"></a>DR drill</p>
</td>
<td class="cellrowborder" valign="top" width="87%" headers="mcps1.2.3.1.2 "><p id="p14161185517308"><a name="p14161185517308"></a><a name="p14161185517308"></a>Is to verify that a DR site server can take over services from a production site server once a failover is performed.</p>
<p id="p3868171511110"><a name="p3868171511110"></a><a name="p3868171511110"></a>In DR drills, you can simulate fault recovery scenarios and formulate emergency recovery plans. When a real fault occurs, the plans can be used to quickly recover services, improving service continuity.</p>
</td>
</tr>
</tbody>
</table>

