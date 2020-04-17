# Querying Details of a Forwarding Policy<a name="EN-US_TOPIC_0136295316"></a>

## Function<a name="section169151579315"></a>

This API is used to query details about a forwarding policy.

## URI<a name="section1221617474435"></a>

GET /v2.0/lbaas/l7policies/\{l7policy\_id\}

**Table  1**  Parameter description

<a name="table158419166402"></a>
<table><thead align="left"><tr id="row19584716114011"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p15841916124016"><a name="p15841916124016"></a><a name="p15841916124016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p454719247712"><a name="p454719247712"></a><a name="p454719247712"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p75841316164014"><a name="p75841316164014"></a><a name="p75841316164014"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p14584151674011"><a name="p14584151674011"></a><a name="p14584151674011"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17158113918463"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p22347125362"><a name="p22347125362"></a><a name="p22347125362"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p145465246716"><a name="p145465246716"></a><a name="p145465246716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p11253185463216"><a name="p11253185463216"></a><a name="p11253185463216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p122341912133616"><a name="p122341912133616"></a><a name="p122341912133616"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section64891616203820"></a>

None

## Response<a name="section1475822284811"></a>

**Table  2**  Response parameters

<a name="table185961183497"></a>
<table><thead align="left"><tr id="row12658108134913"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p46586844919"><a name="p46586844919"></a><a name="p46586844919"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p36581981493"><a name="p36581981493"></a><a name="p36581981493"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p136581817492"><a name="p136581817492"></a><a name="p136581817492"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12658785493"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="a1e31d40522f34b4b847736f330d7177c"><a name="a1e31d40522f34b4b847736f330d7177c"></a><a name="a1e31d40522f34b4b847736f330d7177c"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="a8e35d965d67845119c16270f497fa3c0"><a name="a8e35d965d67845119c16270f497fa3c0"></a><a name="a8e35d965d67845119c16270f497fa3c0"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p16658987498"><a name="p16658987498"></a><a name="p16658987498"></a>Specifies the forwarding policy. For details, see <a href="#table77011444133616">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **l7policy**  parameter description

<a name="table77011444133616"></a>
<table><thead align="left"><tr id="en-us_topic_0136295317_row10701165673714"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0136295317_p1470214562375"><a name="en-us_topic_0136295317_p1470214562375"></a><a name="en-us_topic_0136295317_p1470214562375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0136295317_p2702105618372"><a name="en-us_topic_0136295317_p2702105618372"></a><a name="en-us_topic_0136295317_p2702105618372"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0136295317_p770265613371"><a name="en-us_topic_0136295317_p770265613371"></a><a name="en-us_topic_0136295317_p770265613371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0136295317_row1170211562375"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p37021956163715"><a name="en-us_topic_0136295317_p37021956163715"></a><a name="en-us_topic_0136295317_p37021956163715"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p154311194575"><a name="en-us_topic_0136295317_p154311194575"></a><a name="en-us_topic_0136295317_p154311194575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p87022056103715"><a name="en-us_topic_0136295317_p87022056103715"></a><a name="en-us_topic_0136295317_p87022056103715"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row5702175643718"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p12491330111414"><a name="en-us_topic_0136295317_p12491330111414"></a><a name="en-us_topic_0136295317_p12491330111414"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p1949510305143"><a name="en-us_topic_0136295317_p1949510305143"></a><a name="en-us_topic_0136295317_p1949510305143"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p5927193621418"><a name="en-us_topic_0136295317_p5927193621418"></a><a name="en-us_topic_0136295317_p5927193621418"></a>Specifies the ID of the project where the forwarding policy is used.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row67026562371"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p97021056173713"><a name="en-us_topic_0136295317_p97021056173713"></a><a name="en-us_topic_0136295317_p97021056173713"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p9702105619373"><a name="en-us_topic_0136295317_p9702105619373"></a><a name="en-us_topic_0136295317_p9702105619373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p57021564370"><a name="en-us_topic_0136295317_p57021564370"></a><a name="en-us_topic_0136295317_p57021564370"></a>Specifies the forwarding policy name.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row17021156193714"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p1570220562375"><a name="en-us_topic_0136295317_p1570220562375"></a><a name="en-us_topic_0136295317_p1570220562375"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p270220563373"><a name="en-us_topic_0136295317_p270220563373"></a><a name="en-us_topic_0136295317_p270220563373"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p935075494818"><a name="en-us_topic_0136295317_p935075494818"></a><a name="en-us_topic_0136295317_p935075494818"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="en-us_topic_0136295317_p535095417489"><a name="en-us_topic_0136295317_p535095417489"></a><a name="en-us_topic_0136295317_p535095417489"></a>The value can be <strong id="en-us_topic_0136295317_b12787918559"><a name="en-us_topic_0136295317_b12787918559"></a><a name="en-us_topic_0136295317_b12787918559"></a>true</strong> or <strong id="en-us_topic_0136295317_b1579692551"><a name="en-us_topic_0136295317_b1579692551"></a><a name="en-us_topic_0136295317_b1579692551"></a>false</strong>.</p>
<p id="en-us_topic_0136295317_p1788713318331"><a name="en-us_topic_0136295317_p1788713318331"></a><a name="en-us_topic_0136295317_p1788713318331"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0136295317_b61614114312"><a name="en-us_topic_0136295317_b61614114312"></a><a name="en-us_topic_0136295317_b61614114312"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row87021656103712"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p147021156163720"><a name="en-us_topic_0136295317_p147021156163720"></a><a name="en-us_topic_0136295317_p147021156163720"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p2702105663711"><a name="en-us_topic_0136295317_p2702105663711"></a><a name="en-us_topic_0136295317_p2702105663711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p163501654104816"><a name="en-us_topic_0136295317_p163501654104816"></a><a name="en-us_topic_0136295317_p163501654104816"></a>Provides supplementary information about the forwarding policy.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row1970325673717"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p207031656133714"><a name="en-us_topic_0136295317_p207031656133714"></a><a name="en-us_topic_0136295317_p207031656133714"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p1851734175713"><a name="en-us_topic_0136295317_p1851734175713"></a><a name="en-us_topic_0136295317_p1851734175713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p183501454194816"><a name="en-us_topic_0136295317_p183501454194816"></a><a name="en-us_topic_0136295317_p183501454194816"></a>Specifies the ID of the listener to which the forwarding policy is added.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row1970317567371"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p17703115614375"><a name="en-us_topic_0136295317_p17703115614375"></a><a name="en-us_topic_0136295317_p17703115614375"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p1170365623715"><a name="en-us_topic_0136295317_p1170365623715"></a><a name="en-us_topic_0136295317_p1170365623715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p2351954164814"><a name="en-us_topic_0136295317_p2351954164814"></a><a name="en-us_topic_0136295317_p2351954164814"></a>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</p>
<p id="en-us_topic_0136295317_p13351145412483"><a name="en-us_topic_0136295317_p13351145412483"></a><a name="en-us_topic_0136295317_p13351145412483"></a>The value can be one of the following:</p>
<a name="en-us_topic_0136295317_ul203511354204814"></a><a name="en-us_topic_0136295317_ul203511354204814"></a><ul id="en-us_topic_0136295317_ul203511354204814"><li><strong id="en-us_topic_0136295317_b17722184917467"><a name="en-us_topic_0136295317_b17722184917467"></a><a name="en-us_topic_0136295317_b17722184917467"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to the backend server group specified by <strong id="en-us_topic_0136295317_b372316496462"><a name="en-us_topic_0136295317_b372316496462"></a><a name="en-us_topic_0136295317_b372316496462"></a>redirect_pool_id</strong>.</li><li><strong id="en-us_topic_0136295317_b194119527467"><a name="en-us_topic_0136295317_b194119527467"></a><a name="en-us_topic_0136295317_b194119527467"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected to the HTTPS listener specified by <strong id="en-us_topic_0136295317_b204255216464"><a name="en-us_topic_0136295317_b204255216464"></a><a name="en-us_topic_0136295317_b204255216464"></a>listener_id</strong> to the HTTPS listener specified by <strong id="en-us_topic_0136295317_b114311529462"><a name="en-us_topic_0136295317_b114311529462"></a><a name="en-us_topic_0136295317_b114311529462"></a>redirect_listener_id</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0136295317_row77039560374"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p6703195611375"><a name="en-us_topic_0136295317_p6703195611375"></a><a name="en-us_topic_0136295317_p6703195611375"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p9983113655710"><a name="en-us_topic_0136295317_p9983113655710"></a><a name="en-us_topic_0136295317_p9983113655710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p142211521194918"><a name="en-us_topic_0136295317_p142211521194918"></a><a name="en-us_topic_0136295317_p142211521194918"></a>Specifies the ID of the backend server group to which traffic is forwarded.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row461412820402"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p35992015134018"><a name="en-us_topic_0136295317_p35992015134018"></a><a name="en-us_topic_0136295317_p35992015134018"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p859901512401"><a name="en-us_topic_0136295317_p859901512401"></a><a name="en-us_topic_0136295317_p859901512401"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p722113215492"><a name="en-us_topic_0136295317_p722113215492"></a><a name="en-us_topic_0136295317_p722113215492"></a>Specifies the ID of the listener that forwards the traffic.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row9703135610377"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p18703195613712"><a name="en-us_topic_0136295317_p18703195613712"></a><a name="en-us_topic_0136295317_p18703195613712"></a>redirect_url</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p18703155693720"><a name="en-us_topic_0136295317_p18703155693720"></a><a name="en-us_topic_0136295317_p18703155693720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p1714910214509"><a name="en-us_topic_0136295317_p1714910214509"></a><a name="en-us_topic_0136295317_p1714910214509"></a>Specifies the URL to which traffic is redirected.</p>
<p id="en-us_topic_0136295317_p914972185020"><a name="en-us_topic_0136295317_p914972185020"></a><a name="en-us_topic_0136295317_p914972185020"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row5703956183715"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p18703155613719"><a name="en-us_topic_0136295317_p18703155613719"></a><a name="en-us_topic_0136295317_p18703155613719"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p1970375611378"><a name="en-us_topic_0136295317_p1970375611378"></a><a name="en-us_topic_0136295317_p1970375611378"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p1870195534814"><a name="en-us_topic_0136295317_p1870195534814"></a><a name="en-us_topic_0136295317_p1870195534814"></a>Lists the forwarding rules of the forwarding policy. The following value options are available:</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row1970312566375"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p770375663720"><a name="en-us_topic_0136295317_p770375663720"></a><a name="en-us_topic_0136295317_p770375663720"></a>position</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p1870319564378"><a name="en-us_topic_0136295317_p1870319564378"></a><a name="en-us_topic_0136295317_p1870319564378"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p0275145775019"><a name="en-us_topic_0136295317_p0275145775019"></a><a name="en-us_topic_0136295317_p0275145775019"></a>Specifies the forwarding priority. The value ranges from <strong id="en-us_topic_0136295317_b2339175913554"><a name="en-us_topic_0136295317_b2339175913554"></a><a name="en-us_topic_0136295317_b2339175913554"></a>1</strong> to <strong id="en-us_topic_0136295317_b43407596558"><a name="en-us_topic_0136295317_b43407596558"></a><a name="en-us_topic_0136295317_b43407596558"></a>100</strong>. The default value is <strong id="en-us_topic_0136295317_b842352706165234"><a name="en-us_topic_0136295317_b842352706165234"></a><a name="en-us_topic_0136295317_b842352706165234"></a>100</strong>.</p>
<p id="en-us_topic_0136295317_p122771157115019"><a name="en-us_topic_0136295317_p122771157115019"></a><a name="en-us_topic_0136295317_p122771157115019"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0136295317_row870395643716"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0136295317_p6704256183713"><a name="en-us_topic_0136295317_p6704256183713"></a><a name="en-us_topic_0136295317_p6704256183713"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0136295317_p170405683718"><a name="en-us_topic_0136295317_p170405683718"></a><a name="en-us_topic_0136295317_p170405683718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0136295317_p14704205693714"><a name="en-us_topic_0136295317_p14704205693714"></a><a name="en-us_topic_0136295317_p14704205693714"></a>Specifies the provisioning status of the forwarding policy. The value can be <strong id="en-us_topic_0136295317_b815719212269"><a name="en-us_topic_0136295317_b815719212269"></a><a name="en-us_topic_0136295317_b815719212269"></a>ACTIVE</strong>, <strong id="en-us_topic_0136295317_b116291426162611"><a name="en-us_topic_0136295317_b116291426162611"></a><a name="en-us_topic_0136295317_b116291426162611"></a>PENDING_CREATE</strong>, or <strong id="en-us_topic_0136295317_b95901229192611"><a name="en-us_topic_0136295317_b95901229192611"></a><a name="en-us_topic_0136295317_b95901229192611"></a>ERROR</strong>.</p>
<p id="en-us_topic_0136295317_p178421832011"><a name="en-us_topic_0136295317_p178421832011"></a><a name="en-us_topic_0136295317_p178421832011"></a>The default value is <strong id="en-us_topic_0136295317_b24467134563"><a name="en-us_topic_0136295317_b24467134563"></a><a name="en-us_topic_0136295317_b24467134563"></a>ACTIVE</strong>.</p>
<p id="en-us_topic_0136295317_p210952312206"><a name="en-us_topic_0136295317_p210952312206"></a><a name="en-us_topic_0136295317_p210952312206"></a>This parameter is reserved.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section15975181216365"></a>

-   Example request: Querying details of a forwarding policy

    ```
    GET https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586
    ```

-   Example response

    ```
    {
        "l7policy": {
            "redirect_pool_id": "431a03eb-81bb-408e-ae37-7ce19023692b", 
            "redirect_listener_id": null, 
            "description": "", 
            "admin_state_up": true, 
            "rules": [
                {
                    "id": "67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3"
                }, 
                {
                    "id": "f02b3bca-69d2-4335-a3fa-a8054e996213"
                }
            ], 
            "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819", 
            "listener_id": "26058b64-6185-4e06-874e-4bd68b7633d0", 
            "redirect_url": null, 
            "provisioning_status": "ACTIVE",
            "action": "REDIRECT_TO_POOL", 
            "position": 1, 
            "id": "5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586", 
            "name": "l7policy-garry-1"
        }
    }
    ```


## Status Code<a name="section6200237145116"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

