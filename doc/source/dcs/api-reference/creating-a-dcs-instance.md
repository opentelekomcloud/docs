# Creating a DCS Instance<a name="EN-US_TOPIC_0237964385"></a>

## Function<a name="section10875766"></a>

This API is used to create a DCS instance.

If you create a DCS instance, DCS bills you for the exact volume you actually use.

## URI<a name="section30773030"></a>

-   URI format:

    POST /v1.0/\{project\_id\}/instances

-   Parameter description:

    [Table 1](#table8059334)  describes the parameter of this API.


**Table  1**  Parameter description

<a name="table8059334"></a>
<table><thead align="left"><tr id="row25032404"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.1"><p id="p14358840"><a name="p14358840"></a><a name="p14358840"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.2"><p id="p22215421"><a name="p22215421"></a><a name="p22215421"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="28.28282828282828%" id="mcps1.2.5.1.3"><p id="p54618699"><a name="p54618699"></a><a name="p54618699"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.5.1.4"><p id="p62038473"><a name="p62038473"></a><a name="p62038473"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59060383"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="p19161718"><a name="p19161718"></a><a name="p19161718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.2 "><p id="p8595317"><a name="p8595317"></a><a name="p8595317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="28.28282828282828%" headers="mcps1.2.5.1.3 "><p id="p25132101"><a name="p25132101"></a><a name="p25132101"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.5.1.4 "><p id="p22434318"><a name="p22434318"></a><a name="p22434318"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8521819"></a>

-   Request parameter:

    [Table 2](#table5425146)  describes request parameters.


**Table  2**  Parameter description

<a name="table5425146"></a>
<table><thead align="left"><tr id="row39495638"><th class="cellrowborder" valign="top" width="15.306122448979592%" id="mcps1.2.5.1.1"><p id="p45030147"><a name="p45030147"></a><a name="p45030147"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="11.224489795918368%" id="mcps1.2.5.1.2"><p id="p23563280"><a name="p23563280"></a><a name="p23563280"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="14.285714285714285%" id="mcps1.2.5.1.3"><p id="p29577509"><a name="p29577509"></a><a name="p29577509"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="59.183673469387756%" id="mcps1.2.5.1.4"><p id="p46968043"><a name="p46968043"></a><a name="p46968043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46315145"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p60539304"><a name="p60539304"></a><a name="p60539304"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p4736624"><a name="p4736624"></a><a name="p4736624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p48122248"><a name="p48122248"></a><a name="p48122248"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p5587992"><a name="p5587992"></a><a name="p5587992"></a>DCS instance name.</p>
<p id="p50291933"><a name="p50291933"></a><a name="p50291933"></a>An instance name is a string of 4–64 characters that contain letters, digits, underscores (_), and hyphens (-). An instance name must start with a letter.</p>
</td>
</tr>
<tr id="row49974217"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p21379778"><a name="p21379778"></a><a name="p21379778"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p54040492"><a name="p54040492"></a><a name="p54040492"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p15203759"><a name="p15203759"></a><a name="p15203759"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p23544946"><a name="p23544946"></a><a name="p23544946"></a>Brief description of the DCS instance.</p>
<p id="p10577923"><a name="p10577923"></a><a name="p10577923"></a>A brief description supports up to 1024 characters.</p>
<div class="note" id="note28092445"><a name="note28092445"></a><a name="note28092445"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p51505417"><a name="p51505417"></a><a name="p51505417"></a>"\" is defined as an escape character in the queue description. If you need to enter a backward slash (\) or a double quotation mark (") in the queue description, enter <strong id="b60895577"><a name="b60895577"></a><a name="b60895577"></a>\\</strong> or <strong id="b11189285"><a name="b11189285"></a><a name="b11189285"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row33594701"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p36816290"><a name="p36816290"></a><a name="p36816290"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p29329536"><a name="p29329536"></a><a name="p29329536"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p26882190"><a name="p26882190"></a><a name="p26882190"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p29973748"><a name="p29973748"></a><a name="p29973748"></a>Cache engine, which is Redis.</p>
</td>
</tr>
<tr id="row1328280"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p40481846"><a name="p40481846"></a><a name="p40481846"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p57804097"><a name="p57804097"></a><a name="p57804097"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p51620256"><a name="p51620256"></a><a name="p51620256"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p20491196"><a name="p20491196"></a><a name="p20491196"></a>Cache engine version, which is 3.0.7.</p>
</td>
</tr>
<tr id="row50203036"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p39914077"><a name="p39914077"></a><a name="p39914077"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p11814799"><a name="p11814799"></a><a name="p11814799"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p17474649"><a name="p17474649"></a><a name="p17474649"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p6160484"><a name="p6160484"></a><a name="p6160484"></a>Cache capacity.</p>
<p id="p55444361"><a name="p55444361"></a><a name="p55444361"></a>Unit: GB.</p>
<p id="p29237208"><a name="p29237208"></a><a name="p29237208"></a>For a single-node DCS instance and master/standby DCS instance, the cache capacity can be: 2, 4, 8, 16, 32, or 64 GB.</p>
<p id="p61808280"><a name="p61808280"></a><a name="p61808280"></a>For a DCS instance in cluster mode, the cache capacity can be 64, 128, 256, or 512 GB.</p>
</td>
</tr>
<tr id="row19403611"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p28188696"><a name="p28188696"></a><a name="p28188696"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p1583029"><a name="p1583029"></a><a name="p1583029"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p61116506"><a name="p61116506"></a><a name="p61116506"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p51489968"><a name="p51489968"></a><a name="p51489968"></a>Password of a DCS instance.</p>
<p id="p60756533"><a name="p60756533"></a><a name="p60756533"></a>Password complexity requirements:</p>
<a name="ul9937886"></a><a name="ul9937886"></a><ul id="ul9937886"><li>A string of 8–32 characters.</li><li>Contains at least three of the following character types:<a name="ul64071165"></a><a name="ul64071165"></a><ul id="ul64071165"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters (`~!@#$%^&amp;*()-_=+\|[{}]:'",&lt;.&gt;/?)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row8907181"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p50393070"><a name="p50393070"></a><a name="p50393070"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p55306871"><a name="p55306871"></a><a name="p55306871"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p50671601"><a name="p50671601"></a><a name="p50671601"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p10759044"><a name="p10759044"></a><a name="p10759044"></a>Tenant's VPC ID. For details on how to create VPCs, see the <em id="i29722534"><a name="i29722534"></a><a name="i29722534"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row66176215"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p58673170"><a name="p58673170"></a><a name="p58673170"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p54906334"><a name="p54906334"></a><a name="p54906334"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p18228066"><a name="p18228066"></a><a name="p18228066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p78407"><a name="p78407"></a><a name="p78407"></a>Tenant's security group ID. For details on how to create security groups, see the <em id="i705669"><a name="i705669"></a><a name="i705669"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row6351029"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p44671315"><a name="p44671315"></a><a name="p44671315"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p61606729"><a name="p61606729"></a><a name="p61606729"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p24089152"><a name="p24089152"></a><a name="p24089152"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p5064287"><a name="p5064287"></a><a name="p5064287"></a>Subnet ID. For details on how to create subnets, see the <em id="i45578590"><a name="i45578590"></a><a name="i45578590"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row7554127"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p7904568"><a name="p7904568"></a><a name="p7904568"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p36290241"><a name="p36290241"></a><a name="p36290241"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p53828370"><a name="p53828370"></a><a name="p53828370"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p65130708"><a name="p65130708"></a><a name="p65130708"></a>IDs of the AZs where cache nodes reside. For details on how to query AZs, see <a href="querying-az-information.md">Querying AZ Information</a>.</p>
<div class="note" id="note41095982"><a name="note41095982"></a><a name="note41095982"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p34319524"><a name="p34319524"></a><a name="p34319524"></a>In the current version, only one AZ ID can be set in the request.</p>
</div></div>
</td>
</tr>
<tr id="row40440265"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p54436045"><a name="p54436045"></a><a name="p54436045"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p47243488"><a name="p47243488"></a><a name="p47243488"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p1517357"><a name="p1517357"></a><a name="p1517357"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p55797082"><a name="p55797082"></a><a name="p55797082"></a>Product ID used to differentiate DCS instance types. For details, see <a href="querying-service-specifications.md">Querying Service Specifications</a>.</p>
<p id="p23269775"><a name="p23269775"></a><a name="p23269775"></a>Options:</p>
<a name="ul8101389"></a><a name="ul8101389"></a><ul id="ul8101389"><li>OTC_DCS_SINGLE: indicates a single-node DCS instance.</li><li>OTC_DCS_MS: indicates a master/standby DCS instance.</li><li>OTC_DCS_CL: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row2993363"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p41135882"><a name="p41135882"></a><a name="p41135882"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p43672108"><a name="p43672108"></a><a name="p43672108"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p47779875"><a name="p47779875"></a><a name="p47779875"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p44964695"><a name="p44964695"></a><a name="p44964695"></a>Backup policy.</p>
<p id="p2029075"><a name="p2029075"></a><a name="p2029075"></a>This parameter is available for master/standby DCS instances. For details, see <a href="#table17319656205111">Table 3</a> and <a href="#table1322175615513">Table 4</a>.</p>
</td>
</tr>
<tr id="row2801044"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p25557997"><a name="p25557997"></a><a name="p25557997"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p56931875"><a name="p56931875"></a><a name="p56931875"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p48079133"><a name="p48079133"></a><a name="p48079133"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p2095683"><a name="p2095683"></a><a name="p2095683"></a>Time at which the maintenance time window starts.</p>
<p id="p18861155"><a name="p18861155"></a><a name="p18861155"></a>Format: HH:mm:ss.</p>
<a name="ul35532671"></a><a name="ul35532671"></a><ul id="ul35532671"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see section <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The start time must be set to 22:00:00, 02:00:00, 06:00:00, 10:00:00, 14:00:00, or 18:00: 00.</li><li>Parameters <strong id="b10062570"><a name="b10062570"></a><a name="b10062570"></a>maintain_begin</strong> and <strong id="b23454267"><a name="b23454267"></a><a name="b23454267"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b9761816"><a name="b9761816"></a><a name="b9761816"></a>maintain_start</strong> is left blank, parameter <strong id="b20747480"><a name="b20747480"></a><a name="b20747480"></a>maintain_end</strong> is also blank. In this case, the system automatically allocates the default start time 02:00:00.</li></ul>
</td>
</tr>
<tr id="row52509598"><td class="cellrowborder" valign="top" width="15.306122448979592%" headers="mcps1.2.5.1.1 "><p id="p25419045"><a name="p25419045"></a><a name="p25419045"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="11.224489795918368%" headers="mcps1.2.5.1.2 "><p id="p45676756"><a name="p45676756"></a><a name="p45676756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.285714285714285%" headers="mcps1.2.5.1.3 "><p id="p8829780"><a name="p8829780"></a><a name="p8829780"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59.183673469387756%" headers="mcps1.2.5.1.4 "><p id="p44123597"><a name="p44123597"></a><a name="p44123597"></a>Time at which the maintenance time window ends.</p>
<p id="p61568054"><a name="p61568054"></a><a name="p61568054"></a>Format: HH:mm:ss.</p>
<a name="ul17241574"></a><a name="ul17241574"></a><ul id="ul17241574"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see section <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The end time is four hours later than the start time. For example, if the start time is 22:00:00, the end time is 02:00:00.</li><li>Parameters <strong id="b56237283"><a name="b56237283"></a><a name="b56237283"></a>maintain_begin</strong> and <strong id="b36373507"><a name="b36373507"></a><a name="b36373507"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b58926113"><a name="b58926113"></a><a name="b58926113"></a>maintain_end</strong> is left blank, parameter <strong id="b60572974"><a name="b60572974"></a><a name="b60572974"></a>maintain_start</strong> is also blank. In this case, the system automatically allocates the default end time 06:00:00.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of instance\_backup\_policy

<a name="table17319656205111"></a>
<table><thead align="left"><tr id="row45575417"><th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.1"><p id="p621290"><a name="p621290"></a><a name="p621290"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="7.07070707070707%" id="mcps1.2.5.1.2"><p id="p50324495"><a name="p50324495"></a><a name="p50324495"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11.11111111111111%" id="mcps1.2.5.1.3"><p id="p49752272"><a name="p49752272"></a><a name="p49752272"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="67.67676767676768%" id="mcps1.2.5.1.4"><p id="p3402263"><a name="p3402263"></a><a name="p3402263"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7147849"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p42104912"><a name="p42104912"></a><a name="p42104912"></a>save_days</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p55054740"><a name="p55054740"></a><a name="p55054740"></a>int</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p30248956"><a name="p30248956"></a><a name="p30248956"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p34246385"><a name="p34246385"></a><a name="p34246385"></a>If <strong id="b39782011"><a name="b39782011"></a><a name="b39782011"></a>backup_type</strong> is set to <strong id="b22493786"><a name="b22493786"></a><a name="b22493786"></a>auto</strong>, this parameter is mandatory.</p>
<p id="p1117486"><a name="p1117486"></a><a name="p1117486"></a>Retention time.</p>
<p id="p10057376"><a name="p10057376"></a><a name="p10057376"></a>Unit: day.</p>
<p id="p23407521"><a name="p23407521"></a><a name="p23407521"></a>Value range: 1–7.</p>
</td>
</tr>
<tr id="row9341098"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p18431456"><a name="p18431456"></a><a name="p18431456"></a>backup_type</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p16553004"><a name="p16553004"></a><a name="p16553004"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p65724915"><a name="p65724915"></a><a name="p65724915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p22117919"><a name="p22117919"></a><a name="p22117919"></a>Backup type.</p>
<p id="p64843551"><a name="p64843551"></a><a name="p64843551"></a>Options:</p>
<a name="ul46721048"></a><a name="ul46721048"></a><ul id="ul46721048"><li><strong id="b26308549"><a name="b26308549"></a><a name="b26308549"></a>auto</strong>: automatic backup.</li><li><strong id="b50617743"><a name="b50617743"></a><a name="b50617743"></a>manual</strong>: manual backup.</li></ul>
<p id="p52906506"><a name="p52906506"></a><a name="p52906506"></a>Default value: <strong id="b6396509"><a name="b6396509"></a><a name="b6396509"></a>manual</strong></p>
</td>
</tr>
<tr id="row57568585"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p32543833"><a name="p32543833"></a><a name="p32543833"></a>periodical_backup_plan</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p18804834"><a name="p18804834"></a><a name="p18804834"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p46796555"><a name="p46796555"></a><a name="p46796555"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p32424572"><a name="p32424572"></a><a name="p32424572"></a>Backup plan. For details, see <a href="#table1322175615513">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Parameter description of periodical\_backup\_plan

<a name="table1322175615513"></a>
<table><thead align="left"><tr id="row25469418"><th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.1"><p id="p49757015"><a name="p49757015"></a><a name="p49757015"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="7.07070707070707%" id="mcps1.2.5.1.2"><p id="p3786404"><a name="p3786404"></a><a name="p3786404"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11.11111111111111%" id="mcps1.2.5.1.3"><p id="p38263289"><a name="p38263289"></a><a name="p38263289"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="67.67676767676768%" id="mcps1.2.5.1.4"><p id="p12318719"><a name="p12318719"></a><a name="p12318719"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58292189"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p24046908"><a name="p24046908"></a><a name="p24046908"></a>begin_at</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p1642564"><a name="p1642564"></a><a name="p1642564"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p65938844"><a name="p65938844"></a><a name="p65938844"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p39446124"><a name="p39446124"></a><a name="p39446124"></a>Time at which backup starts.</p>
<p id="p19470801"><a name="p19470801"></a><a name="p19470801"></a>"00:00-01:00" indicates that backup starts at 00:00:00.</p>
</td>
</tr>
<tr id="row41019485"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p34243990"><a name="p34243990"></a><a name="p34243990"></a>period_type</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p22299840"><a name="p22299840"></a><a name="p22299840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p61456643"><a name="p61456643"></a><a name="p61456643"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p11932166"><a name="p11932166"></a><a name="p11932166"></a>Interval at which backup is performed.</p>
<p id="p40280631"><a name="p40280631"></a><a name="p40280631"></a>Currently, only weekly backup is supported.</p>
</td>
</tr>
<tr id="row26981361"><td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.1 "><p id="p38006637"><a name="p38006637"></a><a name="p38006637"></a>backup_at</p>
</td>
<td class="cellrowborder" valign="top" width="7.07070707070707%" headers="mcps1.2.5.1.2 "><p id="p58638753"><a name="p58638753"></a><a name="p58638753"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="11.11111111111111%" headers="mcps1.2.5.1.3 "><p id="p52118582"><a name="p52118582"></a><a name="p52118582"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.67676767676768%" headers="mcps1.2.5.1.4 "><p id="p60855636"><a name="p60855636"></a><a name="p60855636"></a>Day in a week on which backup starts.</p>
<p id="p10829813"><a name="p10829813"></a><a name="p10829813"></a>Value range: 1–7. Where: 1 indicates Monday; 7 indicates Sunday.</p>
</td>
</tr>
</tbody>
</table>

-   Example request for creating a master/standby DCS Redis instance:

    ```
    { 
     "name": "dcs-a11e", 
     "description": "Create a instance", 
     "engine": "Redis", 
     "engine_version": "3.0.7", 
     "capacity": 2, 
     "password": "XXXXXX", 
     "vpc_id": "27d99e17-42f2-4751-818f-5c8c6c03ff15", 
     "security_group_id": "1477393a-29c9-4de5-843f-18ef51257c7e", 
     "subnet_id": "ec2f34b9-20eb-4872-85bd-bea9fc943128", 
     "available_zones": [ 
            "1d7b939b382c4c3bb3481a8ca10da768" 
     ], 
     "product_id": "XXXXXX", 
     "instance_backup_policy": { 
            "save_days": 1, 
            "backup_type": "auto", 
            "periodical_backup_plan": { 
                "begin_at": "00:00-01:00", 
                "period_type": "weekly", 
                "backup_at": [ 
                    1, 
                    2, 
                    3, 
                    4, 
                    5, 
                    6, 
                    7 
                ] 
            } 
     }, 
     "maintain_begin": "22:00:00", 
     "maintain_end": "02:00:00" 
    }
    ```


## Response<a name="section9587508"></a>

If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 5](#table48826322)  describes the response parameter.


**Table  5**  Parameter description

<a name="table48826322"></a>
<table><thead align="left"><tr id="row15564221"><th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.2.4.1.1"><p id="p52742427"><a name="p52742427"></a><a name="p52742427"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.2.4.1.2"><p id="p44278205"><a name="p44278205"></a><a name="p44278205"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.56565656565656%" id="mcps1.2.4.1.3"><p id="p29764876"><a name="p29764876"></a><a name="p29764876"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62144751"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.4.1.1 "><p id="p560079"><a name="p560079"></a><a name="p560079"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.2 "><p id="p45366419"><a name="p45366419"></a><a name="p45366419"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.56565656565656%" headers="mcps1.2.4.1.3 "><p id="p50801316"><a name="p50801316"></a><a name="p50801316"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "instances": [ 
            { 
                "instance_id": "3c49fd6b-fc7c-419e-9644-b6cce008653f", 
                "instance_name": "dcs-a11e" 
            } 
     ], 
     "instance_id": "3c49fd6b-fc7c-419e-9644-b6cce008653f" 
    }
    ```


