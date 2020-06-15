# Updating a Forwarding Policy<a name="EN-US_TOPIC_0136295318"></a>

## Function<a name="section1569947195915"></a>

This API is used to update a forwarding policy. You can select another backend server group or redirect to another HTTPS listener.

## URI<a name="section1131040245"></a>

PUT /v2.0/lbaas/l7policies/\{l7policy\_id\}

**Table  1**  Parameter description

<a name="table158419166402"></a>
<table><thead align="left"><tr id="row19584716114011"><th class="cellrowborder" valign="top" width="16.83168316831683%" id="mcps1.2.5.1.1"><p id="p15841916124016"><a name="p15841916124016"></a><a name="p15841916124016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712869%" id="mcps1.2.5.1.2"><p id="p47391954171517"><a name="p47391954171517"></a><a name="p47391954171517"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.84158415841584%" id="mcps1.2.5.1.3"><p id="p75841316164014"><a name="p75841316164014"></a><a name="p75841316164014"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.45544554455445%" id="mcps1.2.5.1.4"><p id="p616120781615"><a name="p616120781615"></a><a name="p616120781615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17158113918463"><td class="cellrowborder" valign="top" width="16.83168316831683%" headers="mcps1.2.5.1.1 "><p id="p683842913510"><a name="p683842913510"></a><a name="p683842913510"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712869%" headers="mcps1.2.5.1.2 "><p id="p673510547158"><a name="p673510547158"></a><a name="p673510547158"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.84158415841584%" headers="mcps1.2.5.1.3 "><p id="p11229153234917"><a name="p11229153234917"></a><a name="p11229153234917"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455445%" headers="mcps1.2.5.1.4 "><p id="p182291832134920"><a name="p182291832134920"></a><a name="p182291832134920"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section936817221503"></a>

**Table  2**  Request parameters

<a name="t8def61ae804840ce8f73ec72126e9b60"></a>
<table><thead align="left"><tr id="r47185cc7c4804edf84f86a85a2d863f2"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.1"><p id="ad351c1c932af4d5984292bbe732b26f4"><a name="ad351c1c932af4d5984292bbe732b26f4"></a><a name="ad351c1c932af4d5984292bbe732b26f4"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.12121212121212%" id="mcps1.2.5.1.2"><p id="p1339112179160"><a name="p1339112179160"></a><a name="p1339112179160"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.2.5.1.3"><p id="aac928ff36683433e8dc122985e5dcef1"><a name="aac928ff36683433e8dc122985e5dcef1"></a><a name="aac928ff36683433e8dc122985e5dcef1"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.55555555555556%" id="mcps1.2.5.1.4"><p id="a5cb759a9514b4c78b23ab20ff9747d8e"><a name="a5cb759a9514b4c78b23ab20ff9747d8e"></a><a name="a5cb759a9514b4c78b23ab20ff9747d8e"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r77e565bfea25406cb0203115bbcbdd06"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.1 "><p id="ac17113ab943e4d1d946178227509222a"><a name="ac17113ab943e4d1d946178227509222a"></a><a name="ac17113ab943e4d1d946178227509222a"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="12.12121212121212%" headers="mcps1.2.5.1.2 "><p id="p43893171162"><a name="p43893171162"></a><a name="p43893171162"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.2.5.1.3 "><p id="a8448bd3f9f88472982b30f784c2fa33f"><a name="a8448bd3f9f88472982b30f784c2fa33f"></a><a name="a8448bd3f9f88472982b30f784c2fa33f"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.55555555555556%" headers="mcps1.2.5.1.4 "><p id="aeaa137e3a244435fb669482e79ca9c7e"><a name="aeaa137e3a244435fb669482e79ca9c7e"></a><a name="aeaa137e3a244435fb669482e79ca9c7e"></a>Specifies the forwarding policy. For details, see <a href="#table7905034124412">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **l7policy**  parameter description

<a name="table7905034124412"></a>
<table><thead align="left"><tr id="row15979103415441"><th class="cellrowborder" valign="top" width="18.528147185281473%" id="mcps1.2.5.1.1"><p id="p1797913424411"><a name="p1797913424411"></a><a name="p1797913424411"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.358864113588641%" id="mcps1.2.5.1.2"><p id="p997973417442"><a name="p997973417442"></a><a name="p997973417442"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.2.5.1.3"><p id="p997913414445"><a name="p997913414445"></a><a name="p997913414445"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.634536546345366%" id="mcps1.2.5.1.4"><p id="p1597943444411"><a name="p1597943444411"></a><a name="p1597943444411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1197933416441"><td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.2.5.1.1 "><p id="p1197912340445"><a name="p1197912340445"></a><a name="p1197912340445"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="11.358864113588641%" headers="mcps1.2.5.1.2 "><p id="p2979534114413"><a name="p2979534114413"></a><a name="p2979534114413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.2.5.1.3 "><p id="p197913444412"><a name="p197913444412"></a><a name="p197913444412"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.634536546345366%" headers="mcps1.2.5.1.4 "><p id="p12979123414440"><a name="p12979123414440"></a><a name="p12979123414440"></a>Specifies the forwarding policy name.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row4979133417444"><td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.2.5.1.1 "><p id="p15979143415442"><a name="p15979143415442"></a><a name="p15979143415442"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="11.358864113588641%" headers="mcps1.2.5.1.2 "><p id="p1697943412447"><a name="p1697943412447"></a><a name="p1697943412447"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.2.5.1.3 "><p id="p297910347444"><a name="p297910347444"></a><a name="p297910347444"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.634536546345366%" headers="mcps1.2.5.1.4 "><p id="p1979534144414"><a name="p1979534144414"></a><a name="p1979534144414"></a>Provides supplementary information about the forwarding policy.</p>
<p id="p1898874014251"><a name="p1898874014251"></a><a name="p1898874014251"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row179791034174413"><td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.2.5.1.1 "><p id="p9979834184416"><a name="p9979834184416"></a><a name="p9979834184416"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.358864113588641%" headers="mcps1.2.5.1.2 "><p id="p697911348445"><a name="p697911348445"></a><a name="p697911348445"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.2.5.1.3 "><p id="p16541411141712"><a name="p16541411141712"></a><a name="p16541411141712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.634536546345366%" headers="mcps1.2.5.1.4 "><p id="p115216211498"><a name="p115216211498"></a><a name="p115216211498"></a>Specifies the ID of the backend server group to which traffic is forwarded. The default value is <strong id="b11251195282918"><a name="b11251195282918"></a><a name="b11251195282918"></a>null</strong>.</p>
<p id="p1832361213715"><a name="p1832361213715"></a><a name="p1832361213715"></a>This parameter is mandatory when <strong id="b1953719534297"><a name="b1953719534297"></a><a name="b1953719534297"></a>action</strong> is set to <strong id="b0538205342918"><a name="b0538205342918"></a><a name="b0538205342918"></a>REDIRECT_TO_POOL</strong>.</p>
<p id="p4166102318919"><a name="p4166102318919"></a><a name="p4166102318919"></a>This parameter cannot be specified when <strong id="b16225955152914"><a name="b16225955152914"></a><a name="b16225955152914"></a>action</strong> is set to <strong id="b82251655112911"><a name="b82251655112911"></a><a name="b82251655112911"></a>REDIRECT_TO_LISTENER</strong>.</p>
<p id="p92041223986"><a name="p92041223986"></a><a name="p92041223986"></a>The backend server group must meet the following requirements:</p>
<a name="ul15235151117108"></a><a name="ul15235151117108"></a><ul id="ul15235151117108"><li>Cannot be the default backend server group of the listener.</li><li>Cannot be the backend server group used by forwarding policies of other listeners.</li></ul>
</td>
</tr>
<tr id="row8394821144617"><td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.2.5.1.1 "><p id="p11988026154616"><a name="p11988026154616"></a><a name="p11988026154616"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.358864113588641%" headers="mcps1.2.5.1.2 "><p id="p149883264461"><a name="p149883264461"></a><a name="p149883264461"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.2.5.1.3 "><p id="p9166161312179"><a name="p9166161312179"></a><a name="p9166161312179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.634536546345366%" headers="mcps1.2.5.1.4 "><p id="p687911951310"><a name="p687911951310"></a><a name="p687911951310"></a>Specifies the ID of the listener that forwards the traffic. The default value is <strong id="b1832920243013"><a name="b1832920243013"></a><a name="b1832920243013"></a>null</strong>.</p>
<p id="p1736695021210"><a name="p1736695021210"></a><a name="p1736695021210"></a>This parameter is mandatory when <strong id="b19877204183716"><a name="b19877204183716"></a><a name="b19877204183716"></a>action</strong> is set to <strong id="b14878124116378"><a name="b14878124116378"></a><a name="b14878124116378"></a>REDIRECT_TO_LISTENER</strong>.</p>
<p id="p99412422139"><a name="p99412422139"></a><a name="p99412422139"></a>This parameter cannot be specified when <strong id="b440113391373"><a name="b440113391373"></a><a name="b440113391373"></a>action</strong> is set to <strong id="b19402143910374"><a name="b19402143910374"></a><a name="b19402143910374"></a>REDIRECT_TO_POOL</strong>.</p>
<a name="ul17360181816359"></a><a name="ul17360181816359"></a><ul id="ul17360181816359"><li>Can only be an HTTPS listener.</li><li>Can only be a listener of the same load balancer.</li></ul>
</td>
</tr>
<tr id="row718110179816"><td class="cellrowborder" valign="top" width="18.528147185281473%" headers="mcps1.2.5.1.1 "><p id="p1796413221587"><a name="p1796413221587"></a><a name="p1796413221587"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.358864113588641%" headers="mcps1.2.5.1.2 "><p id="p0964922887"><a name="p0964922887"></a><a name="p0964922887"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.2.5.1.3 "><p id="p199641622983"><a name="p199641622983"></a><a name="p199641622983"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.634536546345366%" headers="mcps1.2.5.1.4 "><p id="p09566138386"><a name="p09566138386"></a><a name="p09566138386"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="p10662116133819"><a name="p10662116133819"></a><a name="p10662116133819"></a>The value can be <strong id="b162237579436"><a name="b162237579436"></a><a name="b162237579436"></a>true</strong> or <strong id="b16223457154316"><a name="b16223457154316"></a><a name="b16223457154316"></a>false</strong>.</p>
<p id="p641191819382"><a name="p641191819382"></a><a name="p641191819382"></a>This parameter is reserved. The default value is <strong id="b465120294416"><a name="b465120294416"></a><a name="b465120294416"></a>true</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section243715298217"></a>

**Table  4**  Response parameters

<a name="t3d7d79297f28429b9b1d19f9ae852fc2"></a>
<table><thead align="left"><tr id="re7f7991379e849ab84f21dddacda88e8"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="ab2327df3f66a48f386a031f21e8a7045"><a name="ab2327df3f66a48f386a031f21e8a7045"></a><a name="ab2327df3f66a48f386a031f21e8a7045"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p3364142821710"><a name="p3364142821710"></a><a name="p3364142821710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="aba1653c3e0e64951b79319c9ac7be320"><a name="aba1653c3e0e64951b79319c9ac7be320"></a><a name="aba1653c3e0e64951b79319c9ac7be320"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="p36139447172"><a name="p36139447172"></a><a name="p36139447172"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r25bf6dfff04f4db189e0056f85ce3567"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="a62c8ce32be9a44029528ddc543460f45"><a name="a62c8ce32be9a44029528ddc543460f45"></a><a name="a62c8ce32be9a44029528ddc543460f45"></a>l7policy</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p12363428181713"><a name="p12363428181713"></a><a name="p12363428181713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="ab69ce793f6d34757a62fdda26d8ca8b9"><a name="ab69ce793f6d34757a62fdda26d8ca8b9"></a><a name="ab69ce793f6d34757a62fdda26d8ca8b9"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="ac213dd4d511743518581dd7b53ed5928"><a name="ac213dd4d511743518581dd7b53ed5928"></a><a name="ac213dd4d511743518581dd7b53ed5928"></a>Specifies the forwarding policy. For details, see <a href="#table20746114154514">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **l7policy**  parameter description

<a name="table20746114154514"></a>
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

## Example<a name="section2048983215509"></a>

-   Example request: Updating a forwarding policy

    ```
    PUT https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586
    
    {
        "l7policy": {
            "name": "test"
        }
    }
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
            "action": "REDIRECT_TO_POOL", 
            "provisioning_status": "ACTIVE",
            "position": 2, 
            "id": "5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586", 
            "name": "test"
        }
    }
    ```


## Status Code<a name="section6200237145116"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

