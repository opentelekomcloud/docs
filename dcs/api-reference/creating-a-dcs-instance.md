# Creating a DCS Instance<a name="dcs-api-0312004"></a>

## Function<a name="section682614592540"></a>

This API is used to create a DCS instance.

## URI<a name="section9829541131515"></a>

POST /v1.0/\{project\_id\}/instances

[Table 1](#table9695164612327)  describes the parameter.

**Table  1**  Parameter description

<a name="table9695164612327"></a>
<table><thead align="left"><tr id="row176956462329"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p46951546183217"><a name="p46951546183217"></a><a name="p46951546183217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p8695446203210"><a name="p8695446203210"></a><a name="p8695446203210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p146952046193210"><a name="p146952046193210"></a><a name="p146952046193210"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p36951046133215"><a name="p36951046133215"></a><a name="p36951046133215"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row869515462329"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p106951046173211"><a name="p106951046173211"></a><a name="p106951046173211"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p15695154673220"><a name="p15695154673220"></a><a name="p15695154673220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p969584618324"><a name="p969584618324"></a><a name="p969584618324"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p1069534620323"><a name="p1069534620323"></a><a name="p1069534620323"></a>Project ID. For details on how to obtain the value of this parameter, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section4413221154412"></a>

**Request parameters**

[Table 2](#table56761820495)  describes the request parameters.

**Table  2**  Parameter description

<a name="table56761820495"></a>
<table><thead align="left"><tr id="row767692019916"><th class="cellrowborder" valign="top" width="16.03%" id="mcps1.2.5.1.1"><p id="p136764201394"><a name="p136764201394"></a><a name="p136764201394"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.97%" id="mcps1.2.5.1.2"><p id="p146767206920"><a name="p146767206920"></a><a name="p146767206920"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p5676102012919"><a name="p5676102012919"></a><a name="p5676102012919"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p167618205920"><a name="p167618205920"></a><a name="p167618205920"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row967613201092"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p1867602012910"><a name="p1867602012910"></a><a name="p1867602012910"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p56761920897"><a name="p56761920897"></a><a name="p56761920897"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p156764208911"><a name="p156764208911"></a><a name="p156764208911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p3676820399"><a name="p3676820399"></a><a name="p3676820399"></a>DCS instance name.</p>
<p id="p5676152019920"><a name="p5676152019920"></a><a name="p5676152019920"></a>An instance name is a string of 4 to 64 characters that contain letters, digits, underscores (_), and hyphens (-) and must start with a letter.</p>
</td>
</tr>
<tr id="row1067662016917"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p176763204917"><a name="p176763204917"></a><a name="p176763204917"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p16676020895"><a name="p16676020895"></a><a name="p16676020895"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p106763201696"><a name="p106763201696"></a><a name="p106763201696"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p56765201093"><a name="p56765201093"></a><a name="p56765201093"></a>Brief description of the DCS instance.</p>
<p id="p1967617201791"><a name="p1967617201791"></a><a name="p1967617201791"></a>The description supports up to 1024 characters.</p>
<div class="note" id="note1596631183315"><a name="note1596631183315"></a><a name="note1596631183315"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p396621183310"><a name="p396621183310"></a><a name="p396621183310"></a>The backslash (\) and quotation mark (") are special characters for JSON messages. When using these characters in a parameter value, add the escape character (\) before the characters, for example, <strong id="b65561430311"><a name="b65561430311"></a><a name="b65561430311"></a>\\</strong> and <strong id="b35575315313"><a name="b35575315313"></a><a name="b35575315313"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row2676112013913"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p96778207918"><a name="p96778207918"></a><a name="p96778207918"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p12677320092"><a name="p12677320092"></a><a name="p12677320092"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1567715205914"><a name="p1567715205914"></a><a name="p1567715205914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p118507184116"><a name="p118507184116"></a><a name="p118507184116"></a>Cache engine. Value: <strong id="b19983261307"><a name="b19983261307"></a><a name="b19983261307"></a>Redis</strong>.</p>
</td>
</tr>
<tr id="row196776201292"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p667710200919"><a name="p667710200919"></a><a name="p667710200919"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p1167714202919"><a name="p1167714202919"></a><a name="p1167714202919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p4173155412212"><a name="p4173155412212"></a><a name="p4173155412212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p8892555112"><a name="p8892555112"></a><a name="p8892555112"></a>Cache engine version. Value: <strong id="b168274147117"><a name="b168274147117"></a><a name="b168274147117"></a>3.0</strong>.</p>
</td>
</tr>
<tr id="row567713208916"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p18677112016917"><a name="p18677112016917"></a><a name="p18677112016917"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p1767718205917"><a name="p1767718205917"></a><a name="p1767718205917"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p867782020912"><a name="p867782020912"></a><a name="p867782020912"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p673914475498"><a name="p673914475498"></a><a name="p673914475498"></a>Cache capacity. Unit: GB.</p>
<p id="p1700124711119"><a name="p1700124711119"></a><a name="p1700124711119"></a>For a single-node or master/standby DCS instance, the value can be <strong id="b1920428151019"><a name="b1920428151019"></a><a name="b1920428151019"></a>2</strong>, <strong id="b3204148101015"><a name="b3204148101015"></a><a name="b3204148101015"></a>4</strong>, <strong id="b1420516831015"><a name="b1420516831015"></a><a name="b1420516831015"></a>8</strong>, <strong id="b52053851010"><a name="b52053851010"></a><a name="b52053851010"></a>16</strong>, <strong id="b720614814102"><a name="b720614814102"></a><a name="b720614814102"></a>32</strong>, or <strong id="b1820616881010"><a name="b1820616881010"></a><a name="b1820616881010"></a>64</strong>. For a cluster DCS instance, the value can be <strong id="b72081811107"><a name="b72081811107"></a><a name="b72081811107"></a>64</strong>, <strong id="b1920812812108"><a name="b1920812812108"></a><a name="b1920812812108"></a>128</strong>, <strong id="b1208986109"><a name="b1208986109"></a><a name="b1208986109"></a>256</strong>, or <strong id="b5210683105"><a name="b5210683105"></a><a name="b5210683105"></a>512</strong>.</p>
<a name="ul2084493514411"></a><a name="ul2084493514411"></a>
</td>
</tr>
<tr id="row1067715208919"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p196778201791"><a name="p196778201791"></a><a name="p196778201791"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p46771620993"><a name="p46771620993"></a><a name="p46771620993"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p41909571216"><a name="p41909571216"></a><a name="p41909571216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p19677120192"><a name="p19677120192"></a><a name="p19677120192"></a>Password of a DCS instance.</p>
<p id="p166770201896"><a name="p166770201896"></a><a name="p166770201896"></a>The password of a DCS Redis instance must meet the following complexity requirements:</p>
<a name="ul17145137175920"></a><a name="ul17145137175920"></a><ul id="ul17145137175920"><li>Must be a string consisting of 8 to 32 characters.</li><li>Must be different from the old password.</li><li>Contains at least three of the following character types:<a name="ul81451373599"></a><a name="ul81451373599"></a><ul id="ul81451373599"><li>Lowercase letters</li><li>Uppercase letters</li><li>Digits</li><li>Special characters (`~!@#$%^&amp;*()-_=+\|[{}]:'",&lt;.&gt;/?)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row567822010919"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p1867819201894"><a name="p1867819201894"></a><a name="p1867819201894"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p96788203916"><a name="p96788203916"></a><a name="p96788203916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p66781520294"><a name="p66781520294"></a><a name="p66781520294"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p1714261924017"><a name="p1714261924017"></a><a name="p1714261924017"></a>VPC ID.</p>
<p id="p16517143816118"><a name="p16517143816118"></a><a name="p16517143816118"></a>Obtain the value by using either of the following methods:</p>
<a name="ul887913435377"></a><a name="ul887913435377"></a><ul id="ul887913435377"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: Call the API for querying VPCs. For details, see the "Querying VPCs" section in the <em id="i646410268406"><a name="i646410268406"></a><a name="i646410268406"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row06787201920"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p136781201391"><a name="p136781201391"></a><a name="p136781201391"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p56781204916"><a name="p56781204916"></a><a name="p56781204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p12678120893"><a name="p12678120893"></a><a name="p12678120893"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p8364103564013"><a name="p8364103564013"></a><a name="p8364103564013"></a>ID of the security group which the instance belongs to.</p>
<p id="p1012535151112"><a name="p1012535151112"></a><a name="p1012535151112"></a>Obtain the value by using either of the following methods:</p>
<a name="ul1822354122210"></a><a name="ul1822354122210"></a><ul id="ul1822354122210"><li>Method 1: Log in to VPC console. Choose <strong id="b1731003712515"><a name="b1731003712515"></a><a name="b1731003712515"></a>Access Control</strong> &gt; <strong id="b7315737155115"><a name="b7315737155115"></a><a name="b7315737155115"></a>Security Groups</strong> in the navigation pane on the left. On the displayed page, click the target security group. You can view the security group ID on the displayed page.</li><li>Method 2: Call the API for querying security groups. For details, see the "Querying Security Groups" section in the <em id="i22631413204611"><a name="i22631413204611"></a><a name="i22631413204611"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row867815209918"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p166787201395"><a name="p166787201395"></a><a name="p166787201395"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p3678102018911"><a name="p3678102018911"></a><a name="p3678102018911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p17678132019910"><a name="p17678132019910"></a><a name="p17678132019910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p6957182201210"><a name="p6957182201210"></a><a name="p6957182201210"></a>Network ID of the subnet.</p>
<p id="p394819577568"><a name="p394819577568"></a><a name="p394819577568"></a>Obtain the value by using either of the following methods:</p>
<a name="ul54643814416"></a><a name="ul54643814416"></a><ul id="ul54643814416"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="b13891917475"><a name="b13891917475"></a><a name="b13891917475"></a>Subnets</strong> tab page. You can view the network ID on the displayed page.</li><li>Method 2: Call the API for querying subnets. For details, see the "Querying Subnets" section in the <em id="i8176124810475"><a name="i8176124810475"></a><a name="i8176124810475"></a>Virtual Private Cloud API Reference</em>.</li></ul>
</td>
</tr>
<tr id="row06786202098"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p46783201913"><a name="p46783201913"></a><a name="p46783201913"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p1567815202918"><a name="p1567815202918"></a><a name="p1567815202918"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p567815201913"><a name="p567815201913"></a><a name="p567815201913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p12678420696"><a name="p12678420696"></a><a name="p12678420696"></a>ID of the AZ where the cache node resides and which has available resources. For details on how to obtain the value, see <a href="querying-az-information.md">Querying AZ Information</a>. Check whether the AZ has available resources.</p>
</td>
</tr>
<tr id="row11291932133811"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p114171033193818"><a name="p114171033193818"></a><a name="p114171033193818"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p24171633123817"><a name="p24171633123817"></a><a name="p24171633123817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1541713330384"><a name="p1541713330384"></a><a name="p1541713330384"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p84171833183816"><a name="p84171833183816"></a><a name="p84171833183816"></a>ID of the product that can be created. For details, see <a href="querying-service-specifications.md">Querying Service Specifications</a>.</p>
<div class="p" id="p441713383812"><a name="p441713383812"></a><a name="p441713383812"></a>Options:<a name="ul74175335387"></a><a name="ul74175335387"></a><ul id="ul74175335387"><li><strong id="b944342275510"><a name="b944342275510"></a><a name="b944342275510"></a>OTC_DCS_SINGLE</strong>: indicates a single-node DCS instance.</li><li><strong id="b5855625135512"><a name="b5855625135512"></a><a name="b5855625135512"></a>OTC_DCS_MS</strong>: indicates a master/standby-node DCS instance.</li><li><strong id="b9805102810555"><a name="b9805102810555"></a><a name="b9805102810555"></a>OTC_DCS_CL</strong>: indicates a cluster DCS instance.</li></ul>
</div>
</td>
</tr>
<tr id="row2140102716120"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p978093871216"><a name="p978093871216"></a><a name="p978093871216"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p167801738191210"><a name="p167801738191210"></a><a name="p167801738191210"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p8780143810122"><a name="p8780143810122"></a><a name="p8780143810122"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p2272337113029"><a name="p2272337113029"></a><a name="p2272337113029"></a>Backup policy.</p>
<p id="p792195523714"><a name="p792195523714"></a><a name="p792195523714"></a>This parameter is available for master/standby DCS instances. For details, see <a href="#table12803218151513">Table 3</a> and <a href="#table187492037201518">Table 4</a>.</p>
</td>
</tr>
<tr id="row446514164101"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p153381228151014"><a name="p153381228151014"></a><a name="p153381228151014"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p333802819109"><a name="p333802819109"></a><a name="p333802819109"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p33381928111020"><a name="p33381928111020"></a><a name="p33381928111020"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p66508317113020"><a name="p66508317113020"></a><a name="p66508317113020"></a>Time at which the maintenance time window starts.</p>
<p id="p592955153710"><a name="p592955153710"></a><a name="p592955153710"></a>Format: HH:mm:ss.</p>
<a name="ul933802881010"></a><a name="ul933802881010"></a><ul id="ul933802881010"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-window.md">Querying Maintenance Time Window</a>.</li><li>The start time must be set to 22:00:00, 02:00:00, 06:00:00, 10:00:00, 14:00:00, or 18:00: 00.</li><li>Parameters <strong id="b49724934112956"><a name="b49724934112956"></a><a name="b49724934112956"></a>maintain_begin</strong> and <strong id="b9280265112956"><a name="b9280265112956"></a><a name="b9280265112956"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b24779050112956"><a name="b24779050112956"></a><a name="b24779050112956"></a>maintain_start</strong> is left blank, parameter <strong id="b48544017112956"><a name="b48544017112956"></a><a name="b48544017112956"></a>maintain_end</strong> is also blank. In this case, the system automatically set the start time to 02:00:00.</li></ul>
</td>
</tr>
<tr id="row19206161741015"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.2.5.1.1 "><p id="p17338728191013"><a name="p17338728191013"></a><a name="p17338728191013"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="11.97%" headers="mcps1.2.5.1.2 "><p id="p7338152871019"><a name="p7338152871019"></a><a name="p7338152871019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p63381628181015"><a name="p63381628181015"></a><a name="p63381628181015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p23447854112852"><a name="p23447854112852"></a><a name="p23447854112852"></a>Time at which the maintenance time window ends.</p>
<p id="p49215520376"><a name="p49215520376"></a><a name="p49215520376"></a>Format: HH:mm:ss.</p>
<a name="ul115091720122312"></a><a name="ul115091720122312"></a><ul id="ul115091720122312"><li>The start time and end time of the maintenance time window must indicate the time segment of a supported maintenance time window. For details on how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-window.md">Querying Maintenance Time Window</a>.</li></ul>
<a name="ul93398285106"></a><a name="ul93398285106"></a><ul id="ul93398285106"><li>The end time is four hours later than the start time. For example, if the start time is 22:00:00, the end time is 02:00:00.</li><li>Parameters <strong id="b2895140619279"><a name="b2895140619279"></a><a name="b2895140619279"></a>maintain_begin</strong> and <strong id="b56137128192715"><a name="b56137128192715"></a><a name="b56137128192715"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b170435649711552"><a name="b170435649711552"></a><a name="b170435649711552"></a>maintain_end</strong> is left blank, parameter <strong id="b5799758011552"><a name="b5799758011552"></a><a name="b5799758011552"></a>maintain_start</strong> is also blank. In this case, the system automatically set the end time to 06:00:00.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3**  instance\_backup\_policy parameter description

<a name="table12803218151513"></a>
<table><thead align="left"><tr id="row480331810159"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p0803161819151"><a name="p0803161819151"></a><a name="p0803161819151"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p158036184154"><a name="p158036184154"></a><a name="p158036184154"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p9803181831519"><a name="p9803181831519"></a><a name="p9803181831519"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p1080331819151"><a name="p1080331819151"></a><a name="p1080331819151"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17803111817158"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p980301811156"><a name="p980301811156"></a><a name="p980301811156"></a>save_days</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p280371861517"><a name="p280371861517"></a><a name="p280371861517"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1280314189158"><a name="p1280314189158"></a><a name="p1280314189158"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p17241358195819"><a name="p17241358195819"></a><a name="p17241358195819"></a>This parameter is mandatory when <strong id="b8774547135611"><a name="b8774547135611"></a><a name="b8774547135611"></a>backup_type</strong> is set to <strong id="b54014490562"><a name="b54014490562"></a><a name="b54014490562"></a>manual</strong>.</p>
<p id="p22191059113319"><a name="p22191059113319"></a><a name="p22191059113319"></a>Retention period.</p>
<p id="p49596891113321"><a name="p49596891113321"></a><a name="p49596891113321"></a>Unit: day.</p>
<p id="p992125513371"><a name="p992125513371"></a><a name="p992125513371"></a>Value range: 1–7.</p>
</td>
</tr>
<tr id="row58032184158"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p15803318161514"><a name="p15803318161514"></a><a name="p15803318161514"></a>backup_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p780331841519"><a name="p780331841519"></a><a name="p780331841519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p208031918181519"><a name="p208031918181519"></a><a name="p208031918181519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p12864080113327"><a name="p12864080113327"></a><a name="p12864080113327"></a>Backup type.</p>
<p id="p99265519371"><a name="p99265519371"></a><a name="p99265519371"></a>Options:</p>
<a name="ul14413194210318"></a><a name="ul14413194210318"></a><ul id="ul14413194210318"><li><strong id="b9279681151187"><a name="b9279681151187"></a><a name="b9279681151187"></a>auto</strong>: automatic backup.</li><li><strong id="b16009788721189"><a name="b16009788721189"></a><a name="b16009788721189"></a>manual</strong>: manual backup.</li></ul>
<p id="p1531835311579"><a name="p1531835311579"></a><a name="p1531835311579"></a>The default value is <strong id="b61131248175510"><a name="b61131248175510"></a><a name="b61131248175510"></a>manual</strong>.</p>
</td>
</tr>
<tr id="row58041218181519"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p780421841517"><a name="p780421841517"></a><a name="p780421841517"></a>periodical_backup_plan</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p11804718151519"><a name="p11804718151519"></a><a name="p11804718151519"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1880411821511"><a name="p1880411821511"></a><a name="p1880411821511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p7804101841518"><a name="p7804101841518"></a><a name="p7804101841518"></a>Backup plan. For details, see <a href="#table187492037201518">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  periodical\_backup\_plan parameter description

<a name="table187492037201518"></a>
<table><thead align="left"><tr id="row175053717158"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1675013701519"><a name="p1675013701519"></a><a name="p1675013701519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p18750183701514"><a name="p18750183701514"></a><a name="p18750183701514"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p57501737181518"><a name="p57501737181518"></a><a name="p57501737181518"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p87501837171512"><a name="p87501837171512"></a><a name="p87501837171512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row157502377156"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p117508371150"><a name="p117508371150"></a><a name="p117508371150"></a>begin_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p275013377150"><a name="p275013377150"></a><a name="p275013377150"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p6750133711151"><a name="p6750133711151"></a><a name="p6750133711151"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p54598221113351"><a name="p54598221113351"></a><a name="p54598221113351"></a>Time at which backup starts.</p>
<p id="p1892145513720"><a name="p1892145513720"></a><a name="p1892145513720"></a>"00:00-01:00" indicates that backup starts at 00:00:00.</p>
</td>
</tr>
<tr id="row1975013375150"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p13750193791519"><a name="p13750193791519"></a><a name="p13750193791519"></a>period_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7750133741511"><a name="p7750133741511"></a><a name="p7750133741511"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1075017376159"><a name="p1075017376159"></a><a name="p1075017376159"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p63545920113358"><a name="p63545920113358"></a><a name="p63545920113358"></a>Interval at which backup is performed.</p>
<p id="p1892175583714"><a name="p1892175583714"></a><a name="p1892175583714"></a>Currently, only weekly backup is supported.</p>
</td>
</tr>
<tr id="row18750133715157"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p875112377151"><a name="p875112377151"></a><a name="p875112377151"></a>backup_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p97511037161518"><a name="p97511037161518"></a><a name="p97511037161518"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p18751437171510"><a name="p18751437171510"></a><a name="p18751437171510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p4628573511344"><a name="p4628573511344"></a><a name="p4628573511344"></a>Day in a week on which backup starts.</p>
<p id="p109218555379"><a name="p109218555379"></a><a name="p109218555379"></a>Value range: 1–7, where <strong id="b174365572167"><a name="b174365572167"></a><a name="b174365572167"></a>1</strong> indicates Monday and <strong id="b1915802111718"><a name="b1915802111718"></a><a name="b1915802111718"></a>7</strong> indicates Sunday.</p>
</td>
</tr>
<tr id="row19127254193019"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p191281954163019"><a name="p191281954163019"></a><a name="p191281954163019"></a>timezone_offset</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p3437103311324"><a name="p3437103311324"></a><a name="p3437103311324"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1612913542306"><a name="p1612913542306"></a><a name="p1612913542306"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p25829183113412"><a name="p25829183113412"></a><a name="p25829183113412"></a>Time zone in which backup is performed.</p>
<p id="p1592255153710"><a name="p1592255153710"></a><a name="p1592255153710"></a>Value range: GMT–12:00 to GMT+12:00. If this parameter is left blank, the current time zone of the DCS-Server VM is used by default.</p>
</td>
</tr>
</tbody>
</table>

Example request

Request URL:

```
POST https://{dcs_endpoint}/v1.0/{project_id}/instances
```

-   Example:

    ```
    {
        "name": "dcs-a11e",
        "description": "Create a instance",
        "engine": "Redis",
        "engine_version": "3.0",
        "capacity": 2,
        "password": "XXXXXX",
        "vpc_id": "27d99e17-42f2-4751-818f-5c8c6c03ff15",
        "security_group_id": "1477393a-29c9-4de5-843f-18ef51257c7e",
        "subnet_id": "ec2f34b9-20eb-4872-85bd-bea9fc943128",
        "available_zones": ["ae04cf9d61544df3806a3feeb401b204","d573142f24894ef3bd3664de068b44b0"],
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


## Response<a name="section93113588441"></a>

**Response parameters**

[Table 5](#table079510368334)  describes the response parameters.

**Table  5**  Parameter description

<a name="table079510368334"></a>
<table><thead align="left"><tr id="row187954363335"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p179517363338"><a name="p179517363338"></a><a name="p179517363338"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.2"><p id="p579563643317"><a name="p579563643317"></a><a name="p579563643317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p3795183633313"><a name="p3795183633313"></a><a name="p3795183633313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1379543663318"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p879573633320"><a name="p879573633320"></a><a name="p879573633320"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.2 "><p id="p879573613312"><a name="p879573613312"></a><a name="p879573613312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p179517368331"><a name="p179517368331"></a><a name="p179517368331"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row1147115371915"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p1047185314193"><a name="p1047185314193"></a><a name="p1047185314193"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.2 "><p id="p647175313196"><a name="p647175313196"></a><a name="p647175313196"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p9471353151910"><a name="p9471353151910"></a><a name="p9471353151910"></a>DCS instance list. For details, see <a href="#table128250386224">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6**  Parameter description of the instances array

<a name="table128250386224"></a>
<table><thead align="left"><tr id="row128431538102217"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p5846163852213"><a name="p5846163852213"></a><a name="p5846163852213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p7851173817223"><a name="p7851173817223"></a><a name="p7851173817223"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p15858183862215"><a name="p15858183862215"></a><a name="p15858183862215"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row886183862216"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p16865143815225"><a name="p16865143815225"></a><a name="p16865143815225"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p16872203822215"><a name="p16872203822215"></a><a name="p16872203822215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p158800381229"><a name="p158800381229"></a><a name="p158800381229"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row58828389224"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p4885103815223"><a name="p4885103815223"></a><a name="p4885103815223"></a>instance_name</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p389043832217"><a name="p389043832217"></a><a name="p389043832217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p78973388224"><a name="p78973388224"></a><a name="p78973388224"></a>DCS instance name.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "instances": [
        {
            "instance_id": "3c49fd6b-fc7c-419e-9644-b6cce008653f",
            "instance_name": "dcs-test005"
        }
    ],
    "instance_id": "3c49fd6b-fc7c-419e-9644-b6cce008653f"
}
```

## Status Code<a name="section1837410835217"></a>

[Table 7](#table217814394526)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517). 

**Table  7**  Status code

<a name="table217814394526"></a>
<table><thead align="left"><tr id="row19178103985215"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1817919395523"><a name="p1817919395523"></a><a name="p1817919395523"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p171795391523"><a name="p171795391523"></a><a name="p171795391523"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row617963985216"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p11179113965212"><a name="p11179113965212"></a><a name="p11179113965212"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p1817918393520"><a name="p1817918393520"></a><a name="p1817918393520"></a>DCS instance created successfully.</p>
</td>
</tr>
</tbody>
</table>

