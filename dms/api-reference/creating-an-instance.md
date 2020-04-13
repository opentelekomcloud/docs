# Creating an Instance<a name="EN-US_TOPIC_0128036927"></a>

## Function<a name="section19327142112288"></a>

This API is used to create a Kafka instance.

## URI<a name="section01615217250"></a>

POST /v1.0/\{project\_id\}/instances

[Table 1](#table0211262515)  describes the parameter.

**Table  1**  Parameter description

<a name="table0211262515"></a>
<table><thead align="left"><tr id="row2031516262518"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p631522182516"><a name="p631522182516"></a><a name="p631522182516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p731516272513"><a name="p731516272513"></a><a name="p731516272513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p15315124252"><a name="p15315124252"></a><a name="p15315124252"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p183155252514"><a name="p183155252514"></a><a name="p183155252514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row183151820257"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p731542202515"><a name="p731542202515"></a><a name="p731542202515"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p14315028257"><a name="p14315028257"></a><a name="p14315028257"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p43151224252"><a name="p43151224252"></a><a name="p43151224252"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p10316627259"><a name="p10316627259"></a><a name="p10316627259"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section19344222516"></a>

**Request parameters**

[Table 2](#table63510212250)  describes the parameters.

**Table  2**  Parameter description

<a name="table63510212250"></a>
<table><thead align="left"><tr id="row173161423257"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.1"><p id="p183163211252"><a name="p183163211252"></a><a name="p183163211252"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.2"><p id="p193161422257"><a name="p193161422257"></a><a name="p193161422257"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.3"><p id="p831610215252"><a name="p831610215252"></a><a name="p831610215252"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="58.58585858585859%" id="mcps1.2.5.1.4"><p id="p10316142162517"><a name="p10316142162517"></a><a name="p10316142162517"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18316132152511"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1731618219251"><a name="p1731618219251"></a><a name="p1731618219251"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p1431612210251"><a name="p1431612210251"></a><a name="p1431612210251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p183161727253"><a name="p183161727253"></a><a name="p183161727253"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p14316162182511"><a name="p14316162182511"></a><a name="p14316162182511"></a>Indicates the instance name.</p>
<p id="p53166212252"><a name="p53166212252"></a><a name="p53166212252"></a>An instance name is a string of 4 to 64 characters that contain letters, digits, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row831615212510"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1031652112514"><a name="p1031652112514"></a><a name="p1031652112514"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p931622192514"><a name="p931622192514"></a><a name="p931622192514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p163164282520"><a name="p163164282520"></a><a name="p163164282520"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p63161242514"><a name="p63161242514"></a><a name="p63161242514"></a>Indicates the description of an instance.</p>
<p id="p5316142122513"><a name="p5316142122513"></a><a name="p5316142122513"></a>The description must be a character string containing not more than 1,024 characters.</p>
<div class="note" id="note4439215254"><a name="note4439215254"></a><a name="note4439215254"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p931610214253"><a name="p931610214253"></a><a name="p931610214253"></a>The backslash (\) and quotation mark (") are special characters for JSON packets. When using these characters in a parameter value, add the escape character (\) before these characters, for example, <strong id="b566202855818"><a name="b566202855818"></a><a name="b566202855818"></a>\\</strong> and <strong id="b1427134685817"><a name="b1427134685817"></a><a name="b1427134685817"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row731618292515"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p931813219255"><a name="p931813219255"></a><a name="p931813219255"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p231862182512"><a name="p231862182512"></a><a name="p231862182512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p113188214252"><a name="p113188214252"></a><a name="p113188214252"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p113181222515"><a name="p113181222515"></a><a name="p113181222515"></a>Indicates a message engine. Supported: <strong id="b147734615490"><a name="b147734615490"></a><a name="b147734615490"></a>kafka</strong>.</p>
</td>
</tr>
<tr id="row173189212518"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p17318152162516"><a name="p17318152162516"></a><a name="p17318152162516"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p53181326257"><a name="p53181326257"></a><a name="p53181326257"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p631815214256"><a name="p631815214256"></a><a name="p631815214256"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p1531819212254"><a name="p1531819212254"></a><a name="p1531819212254"></a>Indicates the version of the message engine. Set the value to <strong id="b1892719517557"><a name="b1892719517557"></a><a name="b1892719517557"></a>2.3.0</strong>.</p>
</td>
</tr>
<tr id="row1036171813910"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p10318825257"><a name="p10318825257"></a><a name="p10318825257"></a>storage_space</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p831818217255"><a name="p831818217255"></a><a name="p831818217255"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p2031814215259"><a name="p2031814215259"></a><a name="p2031814215259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p23466313238"><a name="p23466313238"></a><a name="p23466313238"></a>Indicates the message storage space with increments of 100 GB. Unit: GB. Value range:</p>
<a name="ul821611342209"></a><a name="ul821611342209"></a><ul id="ul821611342209"><li>Kafka instance with <strong id="b115011152105519"><a name="b115011152105519"></a><a name="b115011152105519"></a>specification</strong> being <strong id="b16799145565610"><a name="b16799145565610"></a><a name="b16799145565610"></a>100MB</strong>: 600–90,000 GB</li><li>Kafka instance with <strong id="b2041132514576"><a name="b2041132514576"></a><a name="b2041132514576"></a>specification</strong> being <strong id="b1655293115719"><a name="b1655293115719"></a><a name="b1655293115719"></a>300MB</strong>: 1,200–90,000 GB</li><li>Kafka instance with <strong id="b741134535714"><a name="b741134535714"></a><a name="b741134535714"></a>specification</strong> being <strong id="b12661165155714"><a name="b12661165155714"></a><a name="b12661165155714"></a>600MB</strong>: 2,400–90,000 GB</li><li>Kafka instance with <strong id="b1849014155812"><a name="b1849014155812"></a><a name="b1849014155812"></a>specification</strong> being <strong id="b188334619587"><a name="b188334619587"></a><a name="b188334619587"></a>1200MB:</strong> 4,800–90,000 GB</li></ul>
</td>
</tr>
<tr id="row553313413407"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p017271119505"><a name="p017271119505"></a><a name="p017271119505"></a>access_user</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p317720111505"><a name="p317720111505"></a><a name="p317720111505"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p17180111185015"><a name="p17180111185015"></a><a name="p17180111185015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p350512371501"><a name="p350512371501"></a><a name="p350512371501"></a>This parameter is mandatory when <strong id="b165594372520"><a name="b165594372520"></a><a name="b165594372520"></a>engine</strong> is set to <strong id="b17559237185220"><a name="b17559237185220"></a><a name="b17559237185220"></a>kafka</strong> and <strong id="b126211125310"><a name="b126211125310"></a><a name="b126211125310"></a>ssl_enable</strong> is set to <strong id="b13496111315313"><a name="b13496111315313"></a><a name="b13496111315313"></a>true</strong>. This parameter is invalid when <strong id="b6293185117531"><a name="b6293185117531"></a><a name="b6293185117531"></a>ssl_enable</strong> is set to <strong id="b132621659105317"><a name="b132621659105317"></a><a name="b132621659105317"></a>false</strong>.</p>
<p id="p9187911185010"><a name="p9187911185010"></a><a name="p9187911185010"></a>Indicates a username. A username consists of 4 to 64 characters and supports only letters, digits, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="row65341341104016"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1531913213255"><a name="p1531913213255"></a><a name="p1531913213255"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p193199252510"><a name="p193199252510"></a><a name="p193199252510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p6319102122516"><a name="p6319102122516"></a><a name="p6319102122516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p92285164212"><a name="p92285164212"></a><a name="p92285164212"></a>This parameter is mandatory when <strong id="b85299451480"><a name="b85299451480"></a><a name="b85299451480"></a>engine</strong> is set to <strong id="b4529194554814"><a name="b4529194554814"></a><a name="b4529194554814"></a>kafka</strong> and <strong id="b16529184554816"><a name="b16529184554816"></a><a name="b16529184554816"></a>ssl_enable</strong> is set to <strong id="b152974510489"><a name="b152974510489"></a><a name="b152974510489"></a>true</strong>. This parameter is invalid when <strong id="b25298452484"><a name="b25298452484"></a><a name="b25298452484"></a>ssl_enable</strong> is set to <strong id="b205291545154814"><a name="b205291545154814"></a><a name="b205291545154814"></a>false</strong>.</p>
<p id="p18319423255"><a name="p18319423255"></a><a name="p18319423255"></a>Indicates an instance password.</p>
<p id="p1431914282516"><a name="p1431914282516"></a><a name="p1431914282516"></a>An instance password must meet the following complexity requirements:</p>
<a name="ul19319821253"></a><a name="ul19319821253"></a><ul id="ul19319821253"><li>Must be a string consisting of 8 to 32 characters.</li><li>Must contain at least two of the following character types:<a name="ul1645101813412"></a><a name="ul1645101813412"></a><ul id="ul1645101813412"><li>Lowercase letters</li><li>Uppercase letters</li><li>Digits</li><li>Special characters `~!@#$%^&amp;*()-_=+\|[{}];:',&lt;.&gt;/?</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1626054684110"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p831916242511"><a name="p831916242511"></a><a name="p831916242511"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p3319622255"><a name="p3319622255"></a><a name="p3319622255"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p1231912132515"><a name="p1231912132515"></a><a name="p1231912132515"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p123192029258"><a name="p123192029258"></a><a name="p123192029258"></a>Indicates the ID of a VPC.</p>
</td>
</tr>
<tr id="row16260124617419"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p431917292516"><a name="p431917292516"></a><a name="p431917292516"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p83199202517"><a name="p83199202517"></a><a name="p83199202517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p183197222511"><a name="p183197222511"></a><a name="p183197222511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p63196218252"><a name="p63196218252"></a><a name="p63196218252"></a>Indicates the ID of a security group.</p>
</td>
</tr>
<tr id="row126064613413"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1231917222510"><a name="p1231917222510"></a><a name="p1231917222510"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p1831915262513"><a name="p1831915262513"></a><a name="p1831915262513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p1631919282520"><a name="p1631919282520"></a><a name="p1631919282520"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p14319202132519"><a name="p14319202132519"></a><a name="p14319202132519"></a>Indicates the ID of a subnet.</p>
</td>
</tr>
<tr id="row887520744219"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1231982132511"><a name="p1231982132511"></a><a name="p1231982132511"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p03199262517"><a name="p03199262517"></a><a name="p03199262517"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p183191216254"><a name="p183191216254"></a><a name="p183191216254"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p631942102511"><a name="p631942102511"></a><a name="p631942102511"></a>Indicates the ID of an AZ. The parameter value cannot be an empty array or an empty array. For details, see <a href="querying-az-information.md">Querying AZ Information</a>.</p>
</td>
</tr>
<tr id="row387687194210"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p11320172102520"><a name="p11320172102520"></a><a name="p11320172102520"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p332010252511"><a name="p332010252511"></a><a name="p332010252511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p15320524252"><a name="p15320524252"></a><a name="p15320524252"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p3320112182519"><a name="p3320112182519"></a><a name="p3320112182519"></a>Indicates the product ID.</p>
<p id="p1212317503242"><a name="p1212317503242"></a><a name="p1212317503242"></a>For details, see <a href="querying-product-specifications.md">Querying Product Specifications</a>.</p>
</td>
</tr>
<tr id="row1856113944212"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p13320112132514"><a name="p13320112132514"></a><a name="p13320112132514"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p113203216259"><a name="p113203216259"></a><a name="p113203216259"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p18320126252"><a name="p18320126252"></a><a name="p18320126252"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p158729311259"><a name="p158729311259"></a><a name="p158729311259"></a>Indicates the time at which a maintenance time window starts.</p>
<p id="p210962614258"><a name="p210962614258"></a><a name="p210962614258"></a>Format: HH:mm.</p>
<a name="ul1232022112510"></a><a name="ul1232022112510"></a><ul id="ul1232022112510"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details about how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The start time must be set to 22:00, 02:00, 06:00, 10:00, 14:00, or 18:00.</li><li>Parameters <strong id="b5780519142014"><a name="b5780519142014"></a><a name="b5780519142014"></a>maintain_begin</strong> and <strong id="b87804192205"><a name="b87804192205"></a><a name="b87804192205"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b2780151913205"><a name="b2780151913205"></a><a name="b2780151913205"></a>maintain_begin</strong> is left blank, parameter <strong id="b19780171942014"><a name="b19780171942014"></a><a name="b19780171942014"></a>maintain_end</strong> is also left blank. In this case, the system automatically set the start time to 02:00.</li></ul>
</td>
</tr>
<tr id="row1785633984219"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p153201826257"><a name="p153201826257"></a><a name="p153201826257"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p1132019212257"><a name="p1132019212257"></a><a name="p1132019212257"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p9320722251"><a name="p9320722251"></a><a name="p9320722251"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p228514511165"><a name="p228514511165"></a><a name="p228514511165"></a>Indicates the time at which the maintenance time window ends.</p>
<p id="p185352485619"><a name="p185352485619"></a><a name="p185352485619"></a>Format: HH:mm.</p>
<a name="ul1432013292512"></a><a name="ul1432013292512"></a><ul id="ul1432013292512"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details about how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The end time is four hours later than the start time. For example, if the start time is 22:00, the end time is 02:00.</li><li>Parameters <strong id="b3691185833412"><a name="b3691185833412"></a><a name="b3691185833412"></a>maintain_begin</strong> and <strong id="b15691155814348"><a name="b15691155814348"></a><a name="b15691155814348"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b10691145817346"><a name="b10691145817346"></a><a name="b10691145817346"></a>maintain_end</strong> is left blank, parameter <strong id="b14691358153413"><a name="b14691358153413"></a><a name="b14691358153413"></a>maintain_start</strong> is also left blank. In this case, the system automatically set the end time to 06:00.</li></ul>
</td>
</tr>
<tr id="row843717784317"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p144588354614"><a name="p144588354614"></a><a name="p144588354614"></a>ssl_enable</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p9458836469"><a name="p9458836469"></a><a name="p9458836469"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p7458163154618"><a name="p7458163154618"></a><a name="p7458163154618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p112877535115"><a name="p112877535115"></a><a name="p112877535115"></a>Indicates whether to enable SSL-encrypted access.</p>
<a name="ul14751113025120"></a><a name="ul14751113025120"></a><ul id="ul14751113025120"><li><strong id="b17898101144611"><a name="b17898101144611"></a><a name="b17898101144611"></a>true</strong>: enable</li><li><strong id="b173041581467"><a name="b173041581467"></a><a name="b173041581467"></a>false</strong>: disable</li></ul>
</td>
</tr>
<tr id="row1437974434"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p94625574217"><a name="p94625574217"></a><a name="p94625574217"></a>enable_publicip</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p646205584211"><a name="p646205584211"></a><a name="p646205584211"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p15465558422"><a name="p15465558422"></a><a name="p15465558422"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p184635511420"><a name="p184635511420"></a><a name="p184635511420"></a>Indicates whether to enable public access for the instance.</p>
<a name="ul2046195510424"></a><a name="ul2046195510424"></a><ul id="ul2046195510424"><li><strong id="b1557109112915"><a name="b1557109112915"></a><a name="b1557109112915"></a>true</strong>: enable</li><li><strong id="b1197219556363"><a name="b1197219556363"></a><a name="b1197219556363"></a>false</strong>: disable</li></ul>
</td>
</tr>
<tr id="row148031038329"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p18041538929"><a name="p18041538929"></a><a name="p18041538929"></a>public_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p1804938427"><a name="p1804938427"></a><a name="p1804938427"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p9804638323"><a name="p9804638323"></a><a name="p9804638323"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p0804738628"><a name="p0804738628"></a><a name="p0804738628"></a>Indicates the public network bandwidth. Unit: Mbit/s</p>
<p id="p119215503542"><a name="p119215503542"></a><a name="p119215503542"></a>Value range:</p>
<a name="ul242634414559"></a><a name="ul242634414559"></a><ul id="ul242634414559"><li>When <strong id="b13731204215541"><a name="b13731204215541"></a><a name="b13731204215541"></a>specification</strong> is <strong id="b1862794614544"><a name="b1862794614544"></a><a name="b1862794614544"></a>100MB</strong>, the value must be a multiple of 3 in the range from 3 to 900.</li><li>When <strong id="b14310133213574"><a name="b14310133213574"></a><a name="b14310133213574"></a>specification</strong> is <strong id="b7311113225713"><a name="b7311113225713"></a><a name="b7311113225713"></a>300MB</strong>, the value must be a multiple of 3 in the range from 3 to 900.</li><li>When <strong id="b264418575"><a name="b264418575"></a><a name="b264418575"></a>specification</strong> is <strong id="b126204116579"><a name="b126204116579"></a><a name="b126204116579"></a>600MB</strong>, the value must be a multiple of 4 in the range from 4 to 1,200.</li><li>When <strong id="b97331255105716"><a name="b97331255105716"></a><a name="b97331255105716"></a>specification</strong> is <strong id="b673475511573"><a name="b673475511573"></a><a name="b673475511573"></a>1200MB</strong>, the value must be a multiple of 8 in the range from 8 to 2,400.</li></ul>
</td>
</tr>
<tr id="row731910214255"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p196931255164113"><a name="p196931255164113"></a><a name="p196931255164113"></a>retention_policy</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p86911755144111"><a name="p86911755144111"></a><a name="p86911755144111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p468915555417"><a name="p468915555417"></a><a name="p468915555417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p10687115513410"><a name="p10687115513410"></a><a name="p10687115513410"></a>Indicates the action to be taken when the memory usage reaches the disk capacity threshold.</p>
<p id="p19232040171915"><a name="p19232040171915"></a><a name="p19232040171915"></a>Options:</p>
<a name="ul1642771213206"></a><a name="ul1642771213206"></a><ul id="ul1642771213206"><li><strong id="b135294456591"><a name="b135294456591"></a><a name="b135294456591"></a>produce_reject</strong>: New messages cannot be created.</li><li><strong id="b718119563599"><a name="b718119563599"></a><a name="b718119563599"></a>time_base</strong>: The earliest messages are deleted.</li></ul>
</td>
</tr>
<tr id="row18127782467"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p1755018195211"><a name="p1755018195211"></a><a name="p1755018195211"></a>storage_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.2 "><p id="p1655061105213"><a name="p1655061105213"></a><a name="p1655061105213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p555119119524"><a name="p555119119524"></a><a name="p555119119524"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p520913465314"><a name="p520913465314"></a><a name="p520913465314"></a>Indicates the storage I/O specification of a Kafka instance.</p>
<a name="ul15391953193214"></a><a name="ul15391953193214"></a><ul id="ul15391953193214"><li>When <strong id="b810317349481"><a name="b810317349481"></a><a name="b810317349481"></a>specification</strong> is <strong id="b0103634134816"><a name="b0103634134816"></a><a name="b0103634134816"></a>100MB</strong>, the storage I/O can be:<a name="ul10986556152414"></a><a name="ul10986556152414"></a><ul id="ul10986556152414"><li>dms.physical.storage.high</li><li>dms.physical.storage.ultra</li></ul>
</li><li>When <strong id="b259495120491"><a name="b259495120491"></a><a name="b259495120491"></a>specification</strong> is <strong id="b259425115497"><a name="b259425115497"></a><a name="b259425115497"></a>300MB</strong>, the storage I/O can be:<a name="ul44321125257"></a><a name="ul44321125257"></a><ul id="ul44321125257"><li>dms.physical.storage.high</li><li>dms.physical.storage.ultra</li></ul>
</li><li>When <strong id="b7400202311518"><a name="b7400202311518"></a><a name="b7400202311518"></a>specification</strong> is <strong id="b240152317515"><a name="b240152317515"></a><a name="b240152317515"></a>600MB</strong>, the storage I/O is <strong id="b113920339519"><a name="b113920339519"></a><a name="b113920339519"></a>dms.physical.storage.ultra</strong>.</li><li>When <strong id="b15318161565"><a name="b15318161565"></a><a name="b15318161565"></a>specification</strong> is <strong id="b11318511263"><a name="b11318511263"></a><a name="b11318511263"></a>1200MB</strong>, the storage I/O is <strong id="b1330911187611"><a name="b1330911187611"></a><a name="b1330911187611"></a>dms.physical.storage.ultra</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

**Example request for creating a Kafka instance**

```
{
	"name": "kafka-test",
	"description": "",
	"engine": "kafka",
	"engine_version": "2.3.0",
	"storage_space": 600,
	"access_user": "",
	"password": "",
	"vpc_id": "1e93f86e-13af-46c8-97d6-d40fa62b76c2",
	"security_group_id": "0aaa0033-bf7f-4c41-a6c2-18cd04cad2c8",
	"subnet_id": "b5fa806c-35e7-4299-b659-b39398dd4718",
	"available_zones": ["d573142f24894ef3bd3664de068b44b0"],
	"product_id": "00300-30308-0--0",
	"maintain_begin": "22:00",
	"maintain_end": "02:00",
	"ssl_enable": false,
	"enable_publicip": false,
	"publicip_id": "",
	"enterprise_project_id": "0",
	"specification": "100MB",
	"partition_num": "300",
	"retention_policy": "produce_reject",
	"connector_enable": false,
	"storage_spec_code": "dms.physical.storage.ultra"
}
```

## Response<a name="section2013012202516"></a>

**Response parameters**

[Table 3](#table91311217255)  describes the parameters.

**Table  3**  Parameter description

<a name="table91311217255"></a>
<table><thead align="left"><tr id="row1322192152515"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p173221426253"><a name="p173221426253"></a><a name="p173221426253"></a><strong id="b15839173418128"><a name="b15839173418128"></a><a name="b15839173418128"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.2"><p id="p43221521257"><a name="p43221521257"></a><a name="p43221521257"></a><strong id="b11526536181218"><a name="b11526536181218"></a><a name="b11526536181218"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p832217252514"><a name="p832217252514"></a><a name="p832217252514"></a><strong id="b6245183818126"><a name="b6245183818126"></a><a name="b6245183818126"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10322023257"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p832216282518"><a name="p832216282518"></a><a name="p832216282518"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.2 "><p id="p332211219258"><a name="p332211219258"></a><a name="p332211219258"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p123221228259"><a name="p123221228259"></a><a name="p123221228259"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{  
    "instance_id": "8959ab1c-7n1a-yyb1-a05t-93dfc361b32d"  
}
```

## Status Code<a name="section1713714282512"></a>

[Table 4](#table1813714214251)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  4**  Status code

<a name="table1813714214251"></a>
<table><thead align="left"><tr id="row63247232520"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p193241124250"><a name="p193241124250"></a><a name="p193241124250"></a><strong id="b4933203413143"><a name="b4933203413143"></a><a name="b4933203413143"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p17324022258"><a name="p17324022258"></a><a name="p17324022258"></a><strong id="b13949143641412"><a name="b13949143641412"></a><a name="b13949143641412"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row163247212250"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p163245262519"><a name="p163245262519"></a><a name="p163245262519"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p103242213251"><a name="p103242213251"></a><a name="p103242213251"></a>The instance is created successfully.</p>
</td>
</tr>
</tbody>
</table>

