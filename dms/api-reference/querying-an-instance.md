# Querying an Instance<a name="EN-US_TOPIC_0128036896"></a>

## Function<a name="section838810374282"></a>

This API is used to query the details about an instance.

## URI<a name="section972051016372"></a>

GET /v1.0/\{project\_id\}/instances/\{instance\_id\}

[Table 1](#table1372212109375)  describes the parameters.

**Table  1**  Parameter description

<a name="table1372212109375"></a>
<table><thead align="left"><tr id="row1061141116373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1661811103718"><a name="p1661811103718"></a><a name="p1661811103718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.2"><p id="p116110111377"><a name="p116110111377"></a><a name="p116110111377"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.3"><p id="p186191120375"><a name="p186191120375"></a><a name="p186191120375"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.5.1.4"><p id="p461171117376"><a name="p461171117376"></a><a name="p461171117376"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1061111193710"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11612112379"><a name="p11612112379"></a><a name="p11612112379"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.2 "><p id="p11611111183714"><a name="p11611111183714"></a><a name="p11611111183714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p661161119376"><a name="p661161119376"></a><a name="p661161119376"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.4 "><p id="p86111111372"><a name="p86111111372"></a><a name="p86111111372"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row96215114371"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1962111123716"><a name="p1962111123716"></a><a name="p1962111123716"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.2 "><p id="p1262161120373"><a name="p1262161120373"></a><a name="p1262161120373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.3 "><p id="p18628119374"><a name="p18628119374"></a><a name="p18628119374"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.4 "><p id="p1562151119375"><a name="p1562151119375"></a><a name="p1562151119375"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section87301910123719"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section2073021063712"></a>

**Response parameters**

[Table 2](#table873341011371)  describes the parameters.

**Table  2**  Parameter description

<a name="table873341011371"></a>
<table><thead align="left"><tr id="row26210111372"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p1762181153719"><a name="p1762181153719"></a><a name="p1762181153719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p6621911173716"><a name="p6621911173716"></a><a name="p6621911173716"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="p46221119372"><a name="p46221119372"></a><a name="p46221119372"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14621811193717"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p962311183718"><a name="p962311183718"></a><a name="p962311183718"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p2063111163713"><a name="p2063111163713"></a><a name="p2063111163713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p146361163714"><a name="p146361163714"></a><a name="p146361163714"></a>Indicates the instance name.</p>
</td>
</tr>
<tr id="row1263511203717"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p186331123713"><a name="p186331123713"></a><a name="p186331123713"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p3631411153720"><a name="p3631411153720"></a><a name="p3631411153720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p146391143716"><a name="p146391143716"></a><a name="p146391143716"></a>Indicates the message engine.</p>
</td>
</tr>
<tr id="row13631311143716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1563131113375"><a name="p1563131113375"></a><a name="p1563131113375"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p9631611193713"><a name="p9631611193713"></a><a name="p9631611193713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p14635115372"><a name="p14635115372"></a><a name="p14635115372"></a>Indicates the version of the message engine.</p>
</td>
</tr>
<tr id="row116341112371"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1663111113714"><a name="p1663111113714"></a><a name="p1663111113714"></a>specification</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p4631211153713"><a name="p4631211153713"></a><a name="p4631211153713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1063171143716"><a name="p1063171143716"></a><a name="p1063171143716"></a>Indicates the instance specification.</p>
</td>
</tr>
<tr id="row96331183713"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p26321193713"><a name="p26321193713"></a><a name="p26321193713"></a>storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p165161133715"><a name="p165161133715"></a><a name="p165161133715"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p6652011133720"><a name="p6652011133720"></a><a name="p6652011133720"></a>Indicates the message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row68691941845"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1353720132417"><a name="p1353720132417"></a><a name="p1353720132417"></a>partition_num</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p115372131947"><a name="p115372131947"></a><a name="p115372131947"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1053751319418"><a name="p1053751319418"></a><a name="p1053751319418"></a>This parameter is available only for Kafka instances.</p>
<p id="p19537813649"><a name="p19537813649"></a><a name="p19537813649"></a>Indicates the total number of partitions in a Kafka instance.</p>
</td>
</tr>
<tr id="row565151113719"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p26513117379"><a name="p26513117379"></a><a name="p26513117379"></a>used_storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p66561173718"><a name="p66561173718"></a><a name="p66561173718"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p7651711193715"><a name="p7651711193715"></a><a name="p7651711193715"></a>Indicates the used message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row1765101111375"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p865911163713"><a name="p865911163713"></a><a name="p865911163713"></a>connect_address</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p7651211143711"><a name="p7651211143711"></a><a name="p7651211143711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p965161163711"><a name="p965161163711"></a><a name="p965161163711"></a>Indicates the IP address of an instance.</p>
</td>
</tr>
<tr id="row126531110374"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p17653119371"><a name="p17653119371"></a><a name="p17653119371"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p2065911133711"><a name="p2065911133711"></a><a name="p2065911133711"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1651811113714"><a name="p1651811113714"></a><a name="p1651811113714"></a>Indicates the port number of an instance.</p>
</td>
</tr>
<tr id="row1665191119374"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p11654117371"><a name="p11654117371"></a><a name="p11654117371"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1065121115370"><a name="p1065121115370"></a><a name="p1065121115370"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p56531112371"><a name="p56531112371"></a><a name="p56531112371"></a>Indicates the status of an instance. For details, see <a href="instance-status.md">Instance Status</a>.</p>
</td>
</tr>
<tr id="row1865811163716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p76581193713"><a name="p76581193713"></a><a name="p76581193713"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p76521110374"><a name="p76521110374"></a><a name="p76521110374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p46571116371"><a name="p46571116371"></a><a name="p46571116371"></a>Indicates the instance ID.</p>
</td>
</tr>
<tr id="row126512117373"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p965811133717"><a name="p965811133717"></a><a name="p965811133717"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p12651911143711"><a name="p12651911143711"></a><a name="p12651911143711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p176521114379"><a name="p176521114379"></a><a name="p176521114379"></a>Indicates the resource specifications identifier.</p>
<a name="ul265171193719"></a><a name="ul265171193719"></a><ul id="ul265171193719"><li><strong id="b1322913212359"><a name="b1322913212359"></a><a name="b1322913212359"></a>dms.instance.kafka.cluster.c3.mini</strong>: Kafka instance, 100 MB reference bandwidth</li><li><strong id="b145951746350"><a name="b145951746350"></a><a name="b145951746350"></a>dms.instance.kafka.cluster.c3.small.2</strong>: Kafka instance, 300 MB reference bandwidth</li><li><strong id="b121315611358"><a name="b121315611358"></a><a name="b121315611358"></a>dms.instance.kafka.cluster.c3.middle.2</strong>: Kafka instance, 600 MB reference bandwidth</li><li><strong id="b2918121418354"><a name="b2918121418354"></a><a name="b2918121418354"></a>dms.instance.kafka.cluster.c3.high.2</strong>: Kafka instance, 1200 MB reference bandwidth</li></ul>
</td>
</tr>
<tr id="row965211153711"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p136531119370"><a name="p136531119370"></a><a name="p136531119370"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p166511133720"><a name="p166511133720"></a><a name="p166511133720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p3698134971419"><a name="p3698134971419"></a><a name="p3698134971419"></a>For Kafka instances, only <strong id="b0145341152314"><a name="b0145341152314"></a><a name="b0145341152314"></a>cluster</strong> is supported.</p>
</td>
</tr>
<tr id="row15651511123717"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1965151113372"><a name="p1965151113372"></a><a name="p1965151113372"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p176541116371"><a name="p176541116371"></a><a name="p176541116371"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p385716498276"><a name="p385716498276"></a><a name="p385716498276"></a>Billing mode.</p>
</td>
</tr>
<tr id="row10651711143716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p16650116370"><a name="p16650116370"></a><a name="p16650116370"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p116591112371"><a name="p116591112371"></a><a name="p116591112371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p765201110375"><a name="p765201110375"></a><a name="p765201110375"></a>Indicates the ID of a VPC.</p>
</td>
</tr>
<tr id="row16591115374"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1765111163717"><a name="p1765111163717"></a><a name="p1765111163717"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p56651133713"><a name="p56651133713"></a><a name="p56651133713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p10661711183717"><a name="p10661711183717"></a><a name="p10661711183717"></a>Indicates the name of a VPC.</p>
</td>
</tr>
<tr id="row176691123712"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p196601120375"><a name="p196601120375"></a><a name="p196601120375"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1966171163712"><a name="p1966171163712"></a><a name="p1966171163712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p66601112371"><a name="p66601112371"></a><a name="p66601112371"></a>Indicates the time when an instance is created. The time is in the format of timestamp, that is, the offset milliseconds from 1970-01-01 00:00:00 UTC to the specified time.</p>
</td>
</tr>
<tr id="row666141153720"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p136641113711"><a name="p136641113711"></a><a name="p136641113711"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p9661011193716"><a name="p9661011193716"></a><a name="p9661011193716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p66681133712"><a name="p66681133712"></a><a name="p66681133712"></a>Indicates the product ID.</p>
</td>
</tr>
<tr id="row156617113372"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p7667116373"><a name="p7667116373"></a><a name="p7667116373"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1566121123714"><a name="p1566121123714"></a><a name="p1566121123714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p966141113716"><a name="p966141113716"></a><a name="p966141113716"></a>Indicates the security group ID.</p>
</td>
</tr>
<tr id="row866151123716"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p96612117377"><a name="p96612117377"></a><a name="p96612117377"></a>security_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1366211203718"><a name="p1366211203718"></a><a name="p1366211203718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p5661411163716"><a name="p5661411163716"></a><a name="p5661411163716"></a>Indicates the security group name.</p>
</td>
</tr>
<tr id="row196691117379"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p2066111103711"><a name="p2066111103711"></a><a name="p2066111103711"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p366811133711"><a name="p366811133711"></a><a name="p366811133711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1166201143713"><a name="p1166201143713"></a><a name="p1166201143713"></a>Indicates the subnet ID.</p>
</td>
</tr>
<tr id="row16661118374"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p156617118374"><a name="p156617118374"></a><a name="p156617118374"></a>subnet_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p17667115372"><a name="p17667115372"></a><a name="p17667115372"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p136651112378"><a name="p136651112378"></a><a name="p136651112378"></a>Indicates the subnet name.</p>
</td>
</tr>
<tr id="row1968151117375"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p4681911103716"><a name="p4681911103716"></a><a name="p4681911103716"></a>subnet_cidr</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p176861163710"><a name="p176861163710"></a><a name="p176861163710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p4683117375"><a name="p4683117375"></a><a name="p4683117375"></a>Indicates the subnet segment.</p>
</td>
</tr>
<tr id="row268211193718"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p0683116377"><a name="p0683116377"></a><a name="p0683116377"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1168121163713"><a name="p1168121163713"></a><a name="p1168121163713"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p668191116370"><a name="p668191116370"></a><a name="p668191116370"></a>Indicates the ID of the AZ to which the instance node belongs. The AZ ID is returned.</p>
</td>
</tr>
<tr id="row16811163715"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p868181183717"><a name="p868181183717"></a><a name="p868181183717"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1868171111371"><a name="p1868171111371"></a><a name="p1868171111371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p3681611203714"><a name="p3681611203714"></a><a name="p3681611203714"></a>Indicates the user ID.</p>
</td>
</tr>
<tr id="row168201119375"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p18681211153711"><a name="p18681211153711"></a><a name="p18681211153711"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p76810115374"><a name="p76810115374"></a><a name="p76810115374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p068191123712"><a name="p068191123712"></a><a name="p068191123712"></a>Indicates the username.</p>
</td>
</tr>
<tr id="row1482311512122"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p782331591216"><a name="p782331591216"></a><a name="p782331591216"></a>access_user</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p18823715171218"><a name="p18823715171218"></a><a name="p18823715171218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1823181551214"><a name="p1823181551214"></a><a name="p1823181551214"></a>Indicates the username of an instance.</p>
</td>
</tr>
<tr id="row185031349144219"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p9834175713316"><a name="p9834175713316"></a><a name="p9834175713316"></a>total_storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p4834185773111"><a name="p4834185773111"></a><a name="p4834185773111"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p5834105711315"><a name="p5834105711315"></a><a name="p5834105711315"></a>Indicates the message storage space. Unit: GB</p>
</td>
</tr>
<tr id="row19741627144320"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p2516175432812"><a name="p2516175432812"></a><a name="p2516175432812"></a>storage_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p251415413281"><a name="p251415413281"></a><a name="p251415413281"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p651215544286"><a name="p651215544286"></a><a name="p651215544286"></a>Indicates the storage resource ID.</p>
</td>
</tr>
<tr id="row958025174413"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p54253862613"><a name="p54253862613"></a><a name="p54253862613"></a>storage_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p34481152265"><a name="p34481152265"></a><a name="p34481152265"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p194481158263"><a name="p194481158263"></a><a name="p194481158263"></a>Indicates the I/O specification.</p>
</td>
</tr>
<tr id="row5446954114416"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p3875114173517"><a name="p3875114173517"></a><a name="p3875114173517"></a>retention_policy</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p12875114133513"><a name="p12875114133513"></a><a name="p12875114133513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p887534116352"><a name="p887534116352"></a><a name="p887534116352"></a>Indicates the message retention policy.</p>
</td>
</tr>
<tr id="row19255153185015"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p81102403578"><a name="p81102403578"></a><a name="p81102403578"></a>kafka_public_status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p911034065717"><a name="p911034065717"></a><a name="p911034065717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p1211054020574"><a name="p1211054020574"></a><a name="p1211054020574"></a>Indicates whether Kafka public access is enabled.</p>
<a name="ul76284219523"></a><a name="ul76284219523"></a><ul id="ul76284219523"><li><strong id="b13506176203820"><a name="b13506176203820"></a><a name="b13506176203820"></a>true</strong>: Public access is enabled.</li><li><strong id="b1750816245386"><a name="b1750816245386"></a><a name="b1750816245386"></a>false</strong> or <strong id="b171362028103820"><a name="b171362028103820"></a><a name="b171362028103820"></a>closed</strong>: Public access is disabled.</li><li><strong id="b423857143810"><a name="b423857143810"></a><a name="b423857143810"></a>frozen</strong>: Public access configuration is frozen.</li></ul>
</td>
</tr>
<tr id="row112551253115018"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p1319041114588"><a name="p1319041114588"></a><a name="p1319041114588"></a>public_boundwidth</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1719011110583"><a name="p1719011110583"></a><a name="p1719011110583"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p171907114589"><a name="p171907114589"></a><a name="p171907114589"></a>Indicates the public network bandwidth.</p>
</td>
</tr>
<tr id="row14681011193713"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p166811143710"><a name="p166811143710"></a><a name="p166811143710"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1968111123712"><a name="p1968111123712"></a><a name="p1968111123712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p194001012143316"><a name="p194001012143316"></a><a name="p194001012143316"></a>Indicates the time at which a maintenance time window starts.</p>
<p id="p54441822173310"><a name="p54441822173310"></a><a name="p54441822173310"></a>Format: HH:mm</p>
</td>
</tr>
<tr id="row1368111163713"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p96811114371"><a name="p96811114371"></a><a name="p96811114371"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p368191133711"><a name="p368191133711"></a><a name="p368191133711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p513111910337"><a name="p513111910337"></a><a name="p513111910337"></a>Indicates the time at which the maintenance time window ends.</p>
<p id="p5444112213314"><a name="p5444112213314"></a><a name="p5444112213314"></a>Format: HH:mm</p>
</td>
</tr>
<tr id="row19451135165"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p71092245167"><a name="p71092245167"></a><a name="p71092245167"></a>ssl_enable</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p10109162471615"><a name="p10109162471615"></a><a name="p10109162471615"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p71091624131614"><a name="p71091624131614"></a><a name="p71091624131614"></a>Indicates whether to enable security authentication.</p>
<a name="ul10462144102117"></a><a name="ul10462144102117"></a><ul id="ul10462144102117"><li><strong id="b961581083411"><a name="b961581083411"></a><a name="b961581083411"></a>true</strong>: enable</li><li><strong id="b2492393342"><a name="b2492393342"></a><a name="b2492393342"></a>false</strong>: disable</li></ul>
</td>
</tr>
<tr id="row178471142112317"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p63671687358"><a name="p63671687358"></a><a name="p63671687358"></a>service_type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p163673873510"><a name="p163673873510"></a><a name="p163673873510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p183673810358"><a name="p183673810358"></a><a name="p183673810358"></a>Indicates the DMS service type.</p>
</td>
</tr>
<tr id="row22081330162412"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p12367158183514"><a name="p12367158183514"></a><a name="p12367158183514"></a>storage_type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1836818873517"><a name="p1836818873517"></a><a name="p1836818873517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p16368181357"><a name="p16368181357"></a><a name="p16368181357"></a>Indicates the storage type.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error code description

<a name="table7830141043717"></a>
<table><thead align="left"><tr id="row06812117375"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p16689110373"><a name="p16689110373"></a><a name="p16689110373"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p1768111133714"><a name="p1768111133714"></a><a name="p1768111133714"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row136815112375"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p15681211123711"><a name="p15681211123711"></a><a name="p15681211123711"></a>public.00.0001</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p9681011163717"><a name="p9681011163717"></a><a name="p9681011163717"></a>Internal service error.</p>
</td>
</tr>
<tr id="row166813116374"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p36891143716"><a name="p36891143716"></a><a name="p36891143716"></a>public.00.0002</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p568611193719"><a name="p568611193719"></a><a name="p568611193719"></a>Internal service error.</p>
</td>
</tr>
<tr id="row668101103716"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p10681011113711"><a name="p10681011113711"></a><a name="p10681011113711"></a>public.00.0003</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1468151112373"><a name="p1468151112373"></a><a name="p1468151112373"></a>Internal service error.</p>
</td>
</tr>
<tr id="row86816110377"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1568811143714"><a name="p1568811143714"></a><a name="p1568811143714"></a>public.00.0004</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p96815118374"><a name="p96815118374"></a><a name="p96815118374"></a>Failed to create the VPC.</p>
</td>
</tr>
<tr id="row268191112374"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p176871119377"><a name="p176871119377"></a><a name="p176871119377"></a>public.00.0005</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p136819116378"><a name="p136819116378"></a><a name="p136819116378"></a>Failed to create the security group.</p>
</td>
</tr>
<tr id="row56871193712"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p56811119370"><a name="p56811119370"></a><a name="p56811119370"></a>public.00.0006</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1768191119379"><a name="p1768191119379"></a><a name="p1768191119379"></a>Failed to create the subnet.</p>
</td>
</tr>
<tr id="row868181112378"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1683114372"><a name="p1683114372"></a><a name="p1683114372"></a>public.00.0007</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p268311103716"><a name="p268311103716"></a><a name="p268311103716"></a>The subnet status is abnormal.</p>
</td>
</tr>
<tr id="row76891118371"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1868141173717"><a name="p1868141173717"></a><a name="p1868141173717"></a>public.00.0008</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p76801118378"><a name="p76801118378"></a><a name="p76801118378"></a>Failed to create the ECS.</p>
</td>
</tr>
<tr id="row186818112373"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p86841118377"><a name="p86841118377"></a><a name="p86841118377"></a>public.00.0009</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p07081163719"><a name="p07081163719"></a><a name="p07081163719"></a>Failed to create the ECS.</p>
</td>
</tr>
<tr id="row4701411143714"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p67019111377"><a name="p67019111377"></a><a name="p67019111377"></a>public.00.0010</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p197041143718"><a name="p197041143718"></a><a name="p197041143718"></a>Failed to create the ECS.</p>
</td>
</tr>
<tr id="row1970811153718"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p7701311103717"><a name="p7701311103717"></a><a name="p7701311103717"></a>public.00.0011</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2702116374"><a name="p2702116374"></a><a name="p2702116374"></a>Failed to bind an NIC to the ECS.</p>
</td>
</tr>
<tr id="row1170211133719"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1707115374"><a name="p1707115374"></a><a name="p1707115374"></a>public.00.0013</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p970181117373"><a name="p970181117373"></a><a name="p970181117373"></a>Failed to start the ECS.</p>
</td>
</tr>
<tr id="row1709118374"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p187011118378"><a name="p187011118378"></a><a name="p187011118378"></a>public.00.0014</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p470511193717"><a name="p470511193717"></a><a name="p470511193717"></a>Failed to start the ECS.</p>
</td>
</tr>
<tr id="row1070101133720"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p17015114379"><a name="p17015114379"></a><a name="p17015114379"></a>public.00.0015</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p19704115378"><a name="p19704115378"></a><a name="p19704115378"></a>Failed to stop the ECS.</p>
</td>
</tr>
<tr id="row470171103718"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p11701711203718"><a name="p11701711203718"></a><a name="p11701711203718"></a>public.00.0018</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p370191113376"><a name="p370191113376"></a><a name="p370191113376"></a>Failed to create the ECS because the ECS resource quota is insufficient.</p>
</td>
</tr>
<tr id="row3701116370"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p127020118375"><a name="p127020118375"></a><a name="p127020118375"></a>public.00.0024</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p11708119378"><a name="p11708119378"></a><a name="p11708119378"></a>Failed to deploy the instance.</p>
</td>
</tr>
<tr id="row5709113378"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1570141114374"><a name="p1570141114374"></a><a name="p1570141114374"></a>public.00.0025</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p147011143711"><a name="p147011143711"></a><a name="p147011143711"></a>Some nodes of the instance are faulty.</p>
</td>
</tr>
<tr id="row1370121113371"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p470311153712"><a name="p470311153712"></a><a name="p470311153712"></a>public.00.0042</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p77071111375"><a name="p77071111375"></a><a name="p77071111375"></a>Failed to connect to the instance.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

Kafka instance:

```
{
    "name": "kafka-lxy-test",
    "engine": "kafka",
    "port": 9093,
    "status": "RUNNING",
    "type": "cluster",
    "specification": "100MB",
    "engine_version": "2.3.0",
    "connect_address": "192.168.1.239,192.168.1.126,192.168.1.176",
    "instance_id": "8354dde6-8229-4ff4-844d-ab7121be9745",
    "resource_spec_code": "dms.instance.kafka.cluster.c3.mini",
    "charging_mode": 1,
    "vpc_id": "aaa5c155-7a9a-4d92-a804-e19cadcbca63",
    "vpc_name": "vpc-3a7f",
    "created_at": "1572866120990",
    "product_id": "00300-30308-0--0",
    "security_group_id": "3283b880-2256-498c-aa70-154f08f65331",
    "security_group_name": "Default_All",
    "subnet_id": "598d6280-a437-4c2f-9870-a4fc80e7ba66",
    "subnet_name": "subnet-3a7f",
    "subnet_cidr": "192.168.1.0/24",
    "available_zones": [
        "cn-cmcc1b-01"
    ],
    "user_id": "674f286936eb47f28f4fa54b130d4db9",
    "user_name": "hby-cwx522020",
    "access_user": "root",
    "maintain_begin": "22:00:00",
    "maintain_end": "02:00:00",
    "storage_space": 492,
    "total_storage_space": 600,
    "used_storage_space": 25,
    "partition_num": "300",
    "enable_publicip": false,
    "ssl_enable": true,
    "storage_resource_id": "3d737481-04d7-4874-a04b-2b3d884eab99",
    "storage_spec_code": "dms.physical.storage.ultra",
    "service_type": "advanced",
    "storage_type": "hec",
    "retention_policy": "time_base",
    "kafka_public_status": "closed",
    "public_boundwidth": 0
}
```

## Status Code<a name="section1686212108376"></a>

[Table 4](#table1986391010376)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="table1986391010376"></a>
<table><thead align="left"><tr id="row187014114378"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p107011115374"><a name="p107011115374"></a><a name="p107011115374"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p15701311173718"><a name="p15701311173718"></a><a name="p15701311173718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row070121193718"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p5721511153711"><a name="p5721511153711"></a><a name="p5721511153711"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p177211163716"><a name="p177211163716"></a><a name="p177211163716"></a>Specified instance queried successfully.</p>
</td>
</tr>
</tbody>
</table>

